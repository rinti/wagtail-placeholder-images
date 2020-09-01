from django.db import models
from wagtail.core.models import Page
from wagtail.images.models import AbstractImage, Image, AbstractRendition
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images import get_image_model_string
from wagtail_placeholder_images.mixins import PlaceholderRenditionMixin


class CustomImage(PlaceholderRenditionMixin, AbstractImage):
    admin_form_fields = Image.admin_form_fields + (
        # Then add the field names here to make them appear in the form:
        # 'caption',
    )


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(
        CustomImage, related_name="renditions", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)

print(get_image_model_string())


class SomePage(Page):
    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Image",
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("image"),
    ]
