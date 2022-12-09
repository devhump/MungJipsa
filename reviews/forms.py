from django import forms
from .models import Review, Comment, Images
from django.forms.widgets import Textarea
from django.utils.translation import gettext as _


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "content",
        ]
        widgets = {"content": Textarea(attrs={"rows": 4})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
        widgets = {"content": Textarea(attrs={"rows": 4})}


class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = [
            "image",
        ]
        labels = {
            "image": _("Image"),
        }


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label="Search Word")
