from django import forms

from pwdj.galeria.models import Model


class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        exclude = ('foto', )
