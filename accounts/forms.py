from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import Profile, Dog
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "profile",
        )

        labels = {
            "username": "아이디",
            "email": "이메일",
            "password1": "비밀번호",
            "password2": "비밀번호 확인",
            "profile": "사진",
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        fields = (
            "id",
            "email",
            "password1",
            "password2",
            "profile",
        )

        labels = {
            "id": "아이디",
            "email": "이메일",
            "password1": "비밀번호",
            "password2": "비밀번호 확인",
            "profile": "사진",
        }

    # def clean_email(self):
    #     email = self.cleaned_data["email"]
    #     if len(get_user_model().objects.filter(email=email)) >= 2:
    #         raise ValidationError("중복된 이메일이 있습니다.")
    #     return


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["images"]


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog

        fields = (
            "name",
            "dogphoto",
            "gender",
            "neutered",
            "age",
            "personality",
            "dogtype",
        )

        labels = {
            "name": "이름",
            "dogphoto": "사진",
            "gender": "성별",
            "neutered": "중성화 여부",
            "age": "나이",
            "personality": "성격",
            "dogtype": "반려동물 크기",
        }
