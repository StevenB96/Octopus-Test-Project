from rest_framework import serializers

class MeterReadingSerializer(serializers.Serializer):
    """
    Serializer for MeterReading model to produce primitives (for template context).
    """
    id = serializers.IntegerField()
    meter_name = serializers.CharField(source="meter.name")
    reading_value = serializers.DecimalField(max_digits=10, decimal_places=2)
    reading_date = serializers.DateField()
    created_at = serializers.DateTimeField(format=None)