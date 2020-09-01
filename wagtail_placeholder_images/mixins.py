from django.conf import settings
from wagtail.images.models import Filter

from . import Placeholder


class PlaceholderRenditionMixin:

    # def get_placeholder_rendition(self, filter):
    #     if isinstance(filter, str):
    #         filter = Filter(spec=filter)

    #     operation_spec = filter.operations[0]

    #     return Placeholder(spec=operation_spec, img=self)

    def get_placeholder_rendition(self, rendition_filter):
        if isinstance(rendition_filter, str):
            rendition_filter = Filter(spec=rendition_filter)

        available_methods = [
            "width", "height", "fill", "max", "min", "scale", "original"
        ]

        operation = next(filter(lambda x: x.method in available_methods, rendition_filter.operations))
        return Placeholder(spec=operation, img=self)

    def get_rendition(self, filter):
        if getattr(settings, "WAGTAIL_PLACEHOLDERIMAGES_DUMMY", False):
            return self.get_placeholder_rendition(filter)

        return super().get_rendition(filter)
