from django.contrib import admin

# Register your models here.
from .models import Client, Manufacturer, ModelType, Bicycle

admin.site.register(Client)
admin.site.register(Manufacturer)
admin.site.register(ModelType)
admin.site.register(Bicycle)
