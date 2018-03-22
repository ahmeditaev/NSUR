from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.News)
admin.site.register(models.EmailUs)
admin.site.register(models.PressClipping)
admin.site.register(models.PhotoMediaBox)
admin.site.register(models.VideoMediaBox)