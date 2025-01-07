from django.contrib import admin

from .models import Home, Fish
from django.utils.html import format_html


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('name_home', 'description', 'show_photo')
    fields = ['description', 'name_home', ('price', 'photo')]
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        return format_html(f'<img src="{obj.photo.url}" style="max-height: 100px;">')

    show_photo.short_description = 'Фото'


@admin.register(Fish)
class FishAdmin(admin.ModelAdmin):
    list_display = ('name_fish', 'description', 'show_photo')
    fields = ['description', 'name_fish', ('price', 'photo')]
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        return format_html(f'<img src="{obj.photo.url}" style="max-height: 100px;">')

    show_photo.short_description = 'Фото'
