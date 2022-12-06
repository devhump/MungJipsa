from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm, DogForm, DogChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from .models import Dog
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
)
from django.http import JsonResponse


def index(request):
    users = get_user_model().objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(
            request.POST,
            request.FILES,
        )
        if form.is_valid():
            form.save()
            return redirect("accounts:index")

    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("accounts:index")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, "로그아웃 완료")
    return redirect("accounts:index")


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "비밀번호 변경이 성공적으로 완료되었습니다.")
            return redirect("accounts:login")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/password.html", context)


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    messages.success(request, "탈퇴 완료")
    return redirect("accounts:index")


@login_required
@require_http_methods(["GET", "POST"])
def profile(request, username):
    user = get_user_model().objects.get(username=username)
    context = {"user": user}
    return render(request, "accounts/profile.html", context)


@login_required
def update(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if user != request.user:
        return redirect("accounts:index")
    if request.method == "POST" and user == request.user:
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "프로필 정보가 성공적으로 변경되었습니다.")
            return redirect("accounts:index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


@require_POST
def follow(request, username):
    if not request.user.is_authenticated:
        messages.warning(request, "로그인이 필요합니다.")
        return redirect("accounts:login")

    user = get_object_or_404(get_user_model(), username=username)
    if user != request.user:
        if user.followers.filter(username=request.user.username).exists():
            user.followers.remove(request.user)
            is_followed = False
        else:
            user.followers.add(request.user)
            is_followed = True
        # context = {
        # "is_followed": is_followed,
        # "followersCount": user.followers.all().count(),
        # "followingsCount": user.followings.all().count(),
        # }
        # return JsonResponse(context)
    return redirect("accounts:profile", user.username)


@login_required
def dogsignup(request):
    if request.method == "POST":
        forms = DogForm(request.POST, request.FILES)
        if forms.is_valid():
            forms = forms.save(commit=False)
            forms.user = request.user
            forms.save()
            return redirect("accounts:index")
    else:
        forms = DogForm()
    context = {"forms": forms}
    return render(request, "accounts/dogsignup.html", context)


@login_required
def dogdelete(request):
    request.dog.delete()
    messages.success(request, "등록 취소 완료")
    return redirect("accounts:index")


@login_required
def dogupdate(request, dog_pk):
    dog = Dog.objects.get(pk=dog_pk)
    if request.method == "POST":
        form = DogChangeForm(request.POST, request.FILES, instance=dog)
        if form.is_valid() and dog.user == request.user:
            form.save()
            return redirect("accounts:profile", dog.user)
    else:
        form = DogChangeForm(instance=dog)
    context = {
        "form": form,
    }
    return render(request, "accounts/dogupdate.html", context)


@login_required
def dogprofile(request, dog_pk):
    dog = Dog.objects.get(pk=dog_pk)
    context = {"dog": dog}
    return render(request, "accounts/dogprofile.html", context)
