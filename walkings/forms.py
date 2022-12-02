from django import forms
from .models import Mylotations, Dogroup


class MylocationForm(forms.ModelForm):
    class Meta:
        model = Mylotations
        fields = ["location"]


class DogroupForm(forms.ModelForm):
    class Meta:
        model = Dogroup
        fields = [
            "datetime",
            "title",
            "membercnt",
        ]
