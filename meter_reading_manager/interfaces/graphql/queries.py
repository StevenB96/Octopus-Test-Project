# interfaces/graphql/queries.py

import graphene

from meter_reading_manager.domain.meters import queries as meter_queries
from .types import MeterType, MeterReadingType


class Query(graphene.ObjectType):
    """
    Root GraphQL query entrypoints.
    """
    all_meters = graphene.List(MeterType, description="Fetch all meters")
    meter_readings = graphene.List(
        MeterReadingType,
        meter_id=graphene.ID(required=True, description="Meter ID to filter by"),
        description="Fetch all readings for a given meter"
    )

    def resolve_all_meters(self, info):
        # Delegates to domain layer (could add pagination/filters here)
        return meter_queries.list_all_meters()

    def resolve_meter_readings(self, info, meter_id):
        # Delegates to domain layer, ensures readings are sorted
        return meter_queries.get_readings_for_meter(meter_id)
    
'''
# Doc-style GraphQL queries

query GetAllMeters {
  allMeters {
    id
    name
  }
}

query GetReadings($meterId: ID!) {
  meterReadings(meterId: $meterId) {
    id
    readingValue
    readingDate
  }
}
'''
