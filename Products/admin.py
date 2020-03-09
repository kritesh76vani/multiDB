from django.contrib import admin

# Register your models here.

from Products import models as product_model
from django.contrib import admin
from django.db.models.base import ModelBase

# Very hacky!
for name, var in product_model.__dict__.items():
    if type(var) is ModelBase:
        admin.site.register(var)