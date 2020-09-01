[![PyPI version](https://badge.fury.io/py/wagtail-placeholder-images.svg)](https://badge.fury.io/py/wagtail-placeholder-images)

# wagtial placeholder images

This is a package for using placeholder images when developing which can be useful if you're storing them on a server and don't want to download them or link directly to the server when working locally.

## Installation

First download the package:

```sh
pip install wagtail-placeholder-images
```

Then there's two options. If you're using your own custom image model you can use `PlaceholderRenditionMixin` like so:

```python
from wagtail.images.models import AbstractImage
from wagtail_placeholder_images.mixins import PlaceholderRenditionMixin


class CustomImage(PlaceholderRenditionMixin, AbstractImage):
    admin_form_fields = Image.admin_form_fields + (
        # Then add the field names here to make them appear in the form:
        # 'caption',
    )
```

If you're using the standard Wagtail Image model you can monkey patch it:

```python
from wagtail.images.models import AbstractImage
from wagtail_placeholder_images.mixins import PlaceholderRenditionMixin


AbstractImage.get_placeholder_rendition = PlaceholderRenditionMixin.get_placeholder_rendition
AbstractImage.get_rendition = PlaceholderRenditionMixin.get_rendition
```

Then you have to set `WAGTAIL_PLACEHOLDERIMAGES_DUMMY` to `True` and use your desired placeholder source by setting `WAGTAIL_PLACEHOLDERIMAGES_SOURCE`. This should be done in your development settings file, so this doesn't get enabled on your servers. E.g.

```python
# settings_dev.py

WAGTAIL_PLACEHOLDERIMAGES_DUMMY = True
WAGTAIL_PLACEHOLDERIMAGES_SOURCE = "//placedog.net/{width}/{height}/"
```

That should be it!
