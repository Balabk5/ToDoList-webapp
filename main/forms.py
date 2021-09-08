from django.db.models import fields
from main.models import Document
from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="name", max_length=200)
    check = forms.BooleanField(required=False)


class DocumentForm(forms.Form):
    class meta:
        model = Document
        fields = ('description', 'document')
