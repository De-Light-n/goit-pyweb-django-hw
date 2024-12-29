from django import forms

from .models import *


class AuthorForm(forms.ModelForm):
    fullname = forms.CharField(
        min_length=5,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "fullnameInput"}),
    )

    born_date = forms.CharField(
        min_length=8,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "dateBirthInput"}),
    )
    
    born_location = forms.CharField(
        min_length=5,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "locationBirthInput"}),
    )
    
    description = forms.CharField(
        min_length=5,
        widget=forms.Textarea(attrs={"class": "form-control", "id": "descriptionTextarea"}),
    )

    class Meta:
        model = Author
        fields = ("fullname", "born_date", "born_location", "description")


class TagForm(forms.ModelForm):
    name = forms.CharField(
        min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={}),
    )
    
    class Meta:
        model = Tag
        fields = ("name",)


class QuoteForm(forms.ModelForm):
    quote = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={"class": "form-control", "id": "quoteInput"})
    )

    class Meta:
        model = Quote
        fields = ("quote",)
        exclude = ["tags", "author"]
