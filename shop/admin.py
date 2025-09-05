from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Course)

# •	admin.site → the Django admin interface object.
# •	.register(...) → method that tells the admin to include this model.
