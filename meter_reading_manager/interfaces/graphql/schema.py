# interfaces/graphql/schema.py

import graphene

from .queries import Query
from .mutations import Mutation


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    auto_camelcase=True,  # converts snake_case → camelCase in GraphQL API
)
