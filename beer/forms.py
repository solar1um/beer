from django import forms
from beer.models import Generation


class GenForm(forms.ModelForm):
    class Meta:
        model = Generation
        fields = [
            'name',
        ]
