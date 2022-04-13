from django.contrib import admin

from . import models

admin.site.register(models.PostComment)
admin.site.register(models.PostLike)
admin.site.register(models.PostWelfarePlace)


class PostimageInline(admin.TabularInline):
    model = models.PostImage
    extra = 0


class PostCommentInline(admin.TabularInline):
    model = models.PostComment
    extra = 0


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostimageInline, PostCommentInline]
    # list_display = ('title', 'image')
