from django.contrib import admin

from api.models import Manufacturer, ShoeType, ShoeColor, Shoe

admin.register(Manufacturer, ShoeType, ShoeColor, Shoe)(admin.ModelAdmin)