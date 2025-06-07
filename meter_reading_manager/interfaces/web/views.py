# File: meter_reading_manager/interfaces/web/views.py

from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from meter_reading_manager.interfaces.web.forms import MeterReadingForm
from meter_reading_manager.interfaces.web.serialisers import MeterReadingSerializer
from meter_reading_manager.interfaces.tasks.meters.generate_report import generate_report_for_meter
from meter_reading_manager.application.usecases.meters.submit_reading import submit_meter_reading
from meter_reading_manager.domain.meters import queries as meter_queries
from meter_reading_manager.data.models import Meter, MeterReading


class MeterListView(generic.ListView):
    """
    Lists all Meters with their last reading. Uses a Serializer to avoid passing
    rich objects directly into the template.
    """
    template_name = "meters/meter_list.html"
    model = Meter
    context_object_name = "meters"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Build a list of pairs: meter and its last reading (or None)
        meters = context["meters"]
        data = []
        for meter in meters:
            last = meter_queries.get_last_reading(meter)
            if last:
                serialized = MeterReadingSerializer(instance=last).data
            else:
                serialized = None
            data.append({
                "meter_id": meter.id,
                "meter_name": meter.name,
                "last_reading": serialized,
            })

        context["meters_with_readings"] = data
        # Remove the original queryset to avoid accidentally iterating it in template
        context.pop("meters")
        return context


class MeterReadingListView(generic.ListView):
    """
    Displays all readings for a single meter.
    """
    template_name = "meters/meter_readings.html"
    model = MeterReading
    context_object_name = "readings"

    def get_queryset(self):
        meter_id = self.kwargs["meter_id"]
        return MeterReading.objects.filter(meter_id=meter_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        readings = context["readings"]
        # Serialize all readings using our Serializer
        serialized_list = MeterReadingSerializer(instance=readings, many=True).data
        context["readings"] = serialized_list
        context["meter"] = Meter.objects.get(pk=self.kwargs["meter_id"])
        return context


class SubmitReadingView(generic.FormView):
    """
    Renders a form to submit a new MeterReading. On success, redirects to meter detail.
    """
    template_name = "meters/submit_reading.html"
    form_class = MeterReadingForm
    success_url = reverse_lazy("meter-list")

    def form_valid(self, form):
        cleaned = form.cleaned_data
        meter = cleaned["meter"]
        reading_value = cleaned["reading_value"]
        reading_date = cleaned["reading_date"]

        try:
            # Call application layer use-case
            submit_meter_reading(
                meter_id=meter.id,
                reading_value=float(reading_value),
                reading_date=reading_date
            )
        except Exception as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)

        # After successful submission, redirect to the meter's readings page
        return redirect("meter_reading_manager:meter-readings", meter_id=meter.id)


class CreatePdfReportView(generic.View):
    """
    When accessed (e.g. via a button click), this view enqueues a Celery task
    to build and save a PDF report for the given meter_id.
    """

    def post(self, request, *args, **kwargs):
        # Expect meter_id to be passed as part of the URL or POST data
        meter_id = kwargs.get("meter_id")
        meter = get_object_or_404(Meter, pk=meter_id)
        
        # Enqueue the Celery task
        task = generate_report_for_meter.delay(meter_id)

        # You could store task.id somewhere if you want to track status
        messages.success(request, f"Report for '{meter.name}' is being generated in the background.")

        # Redirect back to, e.g., the meter detail page
        return redirect("meter_reading_manager:meter-readings", meter_id=meter_id)