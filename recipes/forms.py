from django import forms
from .models import Recipe

class RecipeSearchForm(forms.Form):
    title = forms.CharField(label="Название", required=False)
    author = forms.CharField(label="Автор", required=False)
