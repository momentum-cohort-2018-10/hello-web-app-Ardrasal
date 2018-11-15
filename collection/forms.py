from django.forms import ModelForm
from collection.models import Place

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'description',)
        