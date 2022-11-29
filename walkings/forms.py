from django import forms
from .models import Mylotations


class MylocationForm(forms.ModelForm):
    class Meta:
        model = Mylotations
        fields = ["location"]
