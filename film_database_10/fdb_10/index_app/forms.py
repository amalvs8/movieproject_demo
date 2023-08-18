from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['f_name', 'f_year', 'f_genre', 'f_prate', 'f_cast', 'f_cast', 'f_dir', 'f_plot', 'f_img']
