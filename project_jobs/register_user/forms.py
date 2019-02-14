from django import forms
from .models import User


class DocumentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'nama', 'email', 'dokumen', )