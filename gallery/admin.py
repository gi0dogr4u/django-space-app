from django.contrib import admin

from gallery.models import Gallery


@admin.register(Gallery)
class GalleryView(admin.ModelAdmin):
    list_display = ["name", "category", "publish", ]
    search_fields = ['name', 'category', ]
    list_filter = ['category', ]
    list_editable = ["publish", ]
    list_per_page = 10
