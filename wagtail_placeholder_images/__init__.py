from django.conf import settings
from django.utils.safestring import mark_safe


class Placeholder:
    def __init__(self, spec, img):
        self.spec = spec
        self.method = spec.method
        self.width = img.width
        self.height = img.height

    def get_height_url(self):
        ratio = self.width / self.height
        new_width = int(self.spec.size * ratio)

        return settings.WAGTAIL_PLACEHOLDERIMAGES_SOURCE.format(
            height=self.spec.size, width=new_width
        )

    def get_width_url(self):
        ratio = self.width / self.height

        new_height = int(self.spec.size / ratio)

        return settings.WAGTAIL_PLACEHOLDERIMAGES_SOURCE.format(
            width=self.spec.size, height=new_height
        )

    def get_scale_url(self):
        ratio = self.spec.percent / 100

        return settings.WAGTAIL_PLACEHOLDERIMAGES_SOURCE.format(
            width=int(self.width * ratio), height=int(self.height * ratio)
        )

    def get_default_url(self):
        width = self.spec.width
        height = self.spec.height
        return settings.WAGTAIL_PLACEHOLDERIMAGES_SOURCE.format(
            width=width, height=height
        )

    def get_original_url(self):
        return settings.WAGTAIL_PLACEHOLDERIMAGES_SOURCE.format(
            width=self.width, height=self.height
        )

    def get_url(self):
        if self.method == "height":
            return self.get_height_url()
        elif self.method == "width":
            return self.get_width_url()
        elif self.method == "scale":
            return self.get_scale_url()
        elif self.method == "original":
            return self.get_original_url()

        return self.get_default_url()

    def img_tag(self, _):
        return mark_safe('<img src="{}">'.format(self.get_url()))
