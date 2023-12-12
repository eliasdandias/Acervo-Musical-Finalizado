from django import forms
from .models import *

# inicializando um formulario para os Albuns
class MusicaForm(forms.ModelForm):
    class Meta:
        # modelo referente: Album
        model = Musica
        # atribuindo todos os campos do modelo Book ao Form
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    class Meta:
        # modelo referente: Album
        model = Album
        # atribuindo todos os campos do modelo Book ao Form
        fields = '__all__'