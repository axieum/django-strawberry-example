from __future__ import annotations

from typing import Iterable

import strawberry
import strawberry_django.mutations
from strawberry_django import NodeInput
from strawberry_django.relay import ListConnectionWithTotalCount

from . import models
from .types import FruitInput, Fruit, FruitInputPartial


@strawberry.type
class FruitQuery:
    """GraphQL queries for fruits."""

    all: ListConnectionWithTotalCount[Fruit] = strawberry_django.connection(description="Query all fruits")

    # @strawberry_django.connection(ListConnectionWithTotalCount[Fruit], description="Query all fruits")
    # def all(self) -> Iterable[models.Fruit]:
    #     return models.Fruit.objects.all()


@strawberry.type
class FruitMutation:
    """GraphQL mutations for fruits."""

    create: Fruit = strawberry_django.mutations.create(FruitInput, description="Create a new fruit")
    update: Fruit = strawberry_django.mutations.update(FruitInputPartial, description="Update an existing fruit")
    delete: Fruit = strawberry_django.mutations.delete(NodeInput, description="Delete a fruit")
