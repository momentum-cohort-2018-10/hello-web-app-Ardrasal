from django.contrib import admin
from collection.models import Places

class PlacesAdmin(admin.ModelAdmin):
    model = Places
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Places, PlacesAdmin)
