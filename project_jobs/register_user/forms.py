from django import forms
from .models import user


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('username', 'document', )