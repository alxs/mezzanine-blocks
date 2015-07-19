from functools import partial

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mezzanine.conf import settings
from .models import (
    BlockCategory,
    Section,
    Block,
    RichBlock,
    ImageBlock,
)


class BlockCategoryAdmin(admin.ModelAdmin):
    ordering = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
    fields = ("title", )


class SectionAdmin(admin.ModelAdmin):
    ordering = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
    fields = ("title", )


class BlockAdmin(admin.ModelAdmin):
    ordering = ('title', 'section', 'category')
    list_display = ('title', 'section', 'category', 'login_required', 'show_title')
    list_editable = ('login_required', 'show_title', 'section', 'category')
    search_fields = ('title', 'content')

    fieldsets = (
        (None, {
            "fields": ["title", "content", ("section", "category")],
        }),
        (_("Advanced data"), {
            "fields": ['login_required', 'show_title', "slug"],
            "classes": ("collapse-closed",)
        }),
    )


class RichBlockAdmin(admin.ModelAdmin):
    ordering = ('title', 'section', 'category')
    list_display = ('title', 'section', 'category', 'show_title')
    list_editable = ('section', 'category')
    list_filter = ('section', 'category')
    search_fields = ('title', 'content')

    fieldsets = (
        (None, {
            "fields": ["title", "content", ("section", "category")],
        }),
        (_("Advanced data"), {
            "fields": ['login_required', 'show_title', "slug"],
            "classes": ("collapse-closed",)
        }),
    )


class ImageBlockAdmin(admin.ModelAdmin):
    ordering = ('title', 'section', 'category')
    list_display = ('admin_thumb', 'title', 'section', 'category', 'height', 'width', 'quality', 'login_required', 'show_title')
    list_display_links = ('admin_thumb', 'title')
    list_editable = ('login_required', 'show_title', 'section', 'category', 'height', 'width', 'quality')
    search_fields = ('title', 'description', 'url')

    fieldsets = (
        (None, {
            "fields": ["title", "description", ("section", "category"), "image", 'url'],
        }),
        (_("Advanced data"), {
            "fields": [('height', 'width', 'quality'), 'login_required', 'show_title', "slug"],
            "classes": ("collapse-closed",)
        }),
    )


def in_menu(app_name):
    """
    Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
    """
    for category, items in settings.ADMIN_MENU_ORDER:
        for item in items:
            if isinstance(item, (tuple, list)):
                if app_name in item:
                    return True
            elif item == app_name:
                return True


BlockCategoryAdmin.in_menu = partial(in_menu, "mezzanine_blocks.BlockCategory")
SectionAdmin.in_menu = partial(in_menu, "mezzanine_blocks.Section")
BlockAdmin.in_menu = partial(in_menu, "mezzanine_blocks.Block")
RichBlockAdmin.in_menu = partial(in_menu, "mezzanine_blocks.RichBlock")
ImageBlockAdmin.in_menu = partial(in_menu, "mezzanine_blocks.ImageBlock")

admin.site.register(BlockCategory, BlockCategoryAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(RichBlock, RichBlockAdmin)
admin.site.register(ImageBlock, ImageBlockAdmin)
