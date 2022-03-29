from django.contrib import admin

from . import models


class CityInline(admin.TabularInline):
    model = models.City
    extra = 0


@admin.register(models.Province)
class ProvinceAdmin(admin.ModelAdmin):
    inlines = [CityInline]
    # list_display = ('title',)
