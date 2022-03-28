from django.contrib import admin

from . import models


class PostimageInline(admin.TabularInline):
    model = models.PostImage


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostimageInline]
    # list_display = ('title', 'image')
