# interfaces/graphql/types.py

import graphene
from graphene_django import DjangoObjectType

from meter_reading_manager.data.models import Meter, MeterReading


class MeterType(DjangoObjectType):
    """GraphQL type for a Meter."""
    class Meta:
        model = Meter
        fields = ("id", "name")


class MeterReadingType(DjangoObjectType):
    """GraphQL type for a MeterReading."""
    class Meta:
        model = MeterReading
        fields = ("id", "meter", "reading_value", "reading_date")


class SubmitReadingInput(graphene.InputObjectType):
    """Input payload for submitting a new meter reading."""
    meter_id      = graphene.ID(required=True, description="The ID of the meter")
    reading_value = graphene.Float(required=True, description="The reading value")
    reading_date  = graphene.Date(required=True, description="Date of the reading")

'''
# Doc-style GraphQL input definition

input SubmitReadingInput {
  meterId: ID!
  readingValue: Float!
  readingDate: Date!
}
'''
