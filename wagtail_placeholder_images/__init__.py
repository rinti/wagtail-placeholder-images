from collections import OrderedDict
from django.conf import settings
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt


class Placeholder:
    def __init__(self, spec, img):
        self.spec = spec
        self.method = spec.method
        self.img = img
        self.calculate_dimensions()

    def calculate_dimensions(self):
        if self.method == "height":
            ratio = self.img.width / self.img.height
            new_width = int(self.spec.size * ratio)
            self.width = new_width
            self.height = self.spec.size
        elif self.method == "width":
            ratio = self.img.width / self.img.height
            new_height = int(self.spec.size / ratio)
            self.width = self.spec.size
            self.height = new_height
        elif self.method == "scale":
            ratio = self.spec.percent / 100
            self.height = int(self.img.height * ratio)
            self.width = int(self.img.width * ratio)
        elif self.method == "original":
            self.height = self.img.height
            self.width = self.img.width
        else:
            self.width = self.spec.width
            self.height = self.spec.height

    def get_url(self):
        return settings.WAGTAIL_PLACEHOLDERIMAGES_SOURCE.format(
            height=self.height, width=self.width
        )

    @property
    def alt(self):
        return "Lorem ipsum"

    @property
    def attrs(self):
        return flatatt(self.attrs_dict)

    @property
    def attrs_dict(self):
        return OrderedDict(
            [
                ("src", self.url),
                ("width", self.width),
                ("height", self.height),
                ("alt", self.alt),
            ]
        )

    @property
    def url(self):
        return self.get_url()

    def img_tag(self, extra_attributes={}):
        attrs = self.attrs_dict.copy()
        attrs.update(extra_attributes)
        return mark_safe('<img{}>'.format(flatatt(attrs)))
