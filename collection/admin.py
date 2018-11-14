from django.contrib import admin
from collection.models import Place

class PlaceAdmin(admin.ModelAdmin):
    model = Place
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Place, PlaceAdmin)
