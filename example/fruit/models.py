from __future__ import annotations

from django.db.models import TextChoices, CharField, Model, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _
from django_choices_field.fields import TextChoicesField
from django_stubs_ext.db.models import TypedModelMeta


class FruitCategory(TextChoices):
    """The category of a fruit."""

    CITRUS = "citrus", "Citrus"
    BERRY = "berry", "Berry"


class Fruit(Model):
    """A tasty treat."""

    name = CharField("name", help_text="The name of the fruit variety", max_length=20)
    category = TextChoicesField(FruitCategory, "category", help_text="The category of the fruit")
    color = ForeignKey(
        "Color",
        verbose_name="colour",
        help_text="The colour of this kind of fruit",
        on_delete=CASCADE,
        related_name="fruits",
        blank=True,
        null=True,
    )

    class Meta(TypedModelMeta):
        verbose_name = "fruit"
        verbose_name_plural = "fruits"
        ordering = ("name",)


class Color(Model):
    """The hue of your tasty treat."""

    name = CharField("name", help_text="The colour name", max_length=20)

    class Meta(TypedModelMeta):
        verbose_name = "colour"
        verbose_name_plural = "colours"
        ordering = ("name",)
