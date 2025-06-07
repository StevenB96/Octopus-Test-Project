# interfaces/graphql/mutations.py

import graphene

from meter_reading_manager.application.usecases.meters.submit_reading import submit_meter_reading
from .types import MeterReadingType, SubmitReadingInput


class SubmitReading(graphene.Mutation):
    """
    Mutation to submit a new reading for a meter.
    Reuses the `submit_meter_reading` use-case from the application layer.
    """
    class Arguments:
        input = SubmitReadingInput(required=True)

    ok      = graphene.Boolean(description="True if submission succeeded")
    reading = graphene.Field(MeterReadingType, description="The newly created reading")
    errors  = graphene.List(graphene.String, description="List of error messages, if any")

    @classmethod
    def mutate(cls, root, info, input):
        try:
            reading = submit_meter_reading(
                meter_id      = input.meter_id,
                reading_value = input.reading_value,
                reading_date  = input.reading_date,
            )
            return cls(ok=True, reading=reading, errors=[])
        except Exception as exc:
            return cls(ok=False, reading=None, errors=[str(exc)])


class Mutation(graphene.ObjectType):
    """
    Root GraphQL mutations.
    """
    submit_reading = SubmitReading.Field(description="Submit a meter reading")

'''
# Doc-style GraphQL mutation

mutation SubmitReadingMutation($input: SubmitReadingInput!) {
  submitReading(input: $input) {
    ok
    reading {
      id
      meter {
        id
        name
      }
      readingValue
      readingDate
    }
    errors
  }
}

'''
