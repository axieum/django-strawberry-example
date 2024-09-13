from __future__ import annotations

import strawberry
from django.conf import settings
from strawberry.extensions import QueryDepthLimiter, MaxAliasesLimiter, MaxTokensLimiter
from strawberry_django.optimizer import DjangoOptimizerExtension

from .fruit.schema import FruitQuery


@strawberry.type
class Query:
    """All GraphQL queries."""

    fruits: FruitQuery = strawberry.field(resolver=FruitQuery, description="Query fruits")


@strawberry.type
class Mutation:
    """All GraphQL mutations."""

    # fruits: FruitMutation = strawberry.field(resolver=FruitMutation, description="Mutate fruits")


# The Django Strawberry GraphQL schema.
schema = strawberry.Schema(
    query=Query,
    # mutation=Mutation,
    extensions=(
        QueryDepthLimiter(max_depth=settings.STRAWBERRY_DJANGO["_QUERY_DEPTH_LIMIT"]),
        MaxAliasesLimiter(max_alias_count=settings.STRAWBERRY_DJANGO["_ALIAS_COUNT_LIMIT"]),
        MaxTokensLimiter(max_token_count=settings.STRAWBERRY_DJANGO["_TOKEN_COUNT_LIMIT"]),
        DjangoOptimizerExtension(),
    ),
)
