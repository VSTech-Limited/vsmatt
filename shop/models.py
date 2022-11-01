import os

# Create your models here.


TAGS_IMAGES_PATH = os.path.join("uploads", "shop", "tags")


def tag_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.id, ext)
    return os.path.join(TAGS_IMAGES_PATH, filename)

# https://youtu.be/_vCT42vDfgw
