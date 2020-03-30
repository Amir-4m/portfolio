import random
import os

from django.db import models


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(null=True, default='description')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    in_progress = models.BooleanField(default=False)
    project_url = models.URLField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
