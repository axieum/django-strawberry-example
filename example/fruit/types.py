from __future__ import annotations

import strawberry_django
from strawberry import auto
from strawberry.relay import Node
from strawberry_django import NodeInput

from . import models


@strawberry_django.type(models.Fruit)
class Fruit(Node):
    """A tasty treat."""

    name: auto
    category: auto
    color: Color | None


@strawberry_django.input(models.Fruit)
class FruitInput:
    """A tasty treat input."""

    name: auto
    category: auto
    color: ColorInput | None


@strawberry_django.partial(models.Fruit)
class FruitInputPartial(NodeInput):
    """A tasty treat partial input."""

    name: auto
    category: auto
    color: ColorInput | None


@strawberry_django.type(models.Color)
class Color(Node):
    """The hue of your tasty treat."""

    name: auto
    fruits: list[Fruit]


@strawberry_django.input(models.Color)
class ColorInput:
    """A tasty treat input."""

    name: auto


@strawberry_django.partial(models.Color)
class ColorInputPartial(NodeInput):
    """A tasty treat partial input."""

    name: auto
