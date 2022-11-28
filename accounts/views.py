from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, DogForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


def index(request):
    users = get_user_model().objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(
            request.POST, request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def dogsignup(request):
    if request.method == "POST":
        forms = DogForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect("accounts:index")
    else:
        forms = DogForm()
    context = {"forms": forms}
    return render(request, "accounts/dogsignup.html", context)


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
@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "프로필 정보가 성공적으로 변경되었습니다.")
            return redirect("accounts:profile", request.user.username)
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
    return redirect("index")


@login_required
def profile(request):
    user_ = request.user
    profile_ = user_.profile_set.all()[0]
    print(profile_)
    context = {
        "profile": profile_,
        "reviews": request.user.review_set.all(),
    }
    return render(request, "accounts/profile.html", context)


# @login_required
# def profile_update(request):
#     user_ = get_user_model().objects.get(pk=request.user.pk)
#     current_user = user_.profile_set.all()[0]
#     if request.method == "POST":
#         form = ProfileForm(request.POST, request.FILES, instance=current_user)
#         if form.is_valid():
#             form.save()
#             return redirect("accounts:profile")
#     else:
#         form = ProfileForm(instance=current_user)
#     context = {
#         "profile_form": form,
#     }
#     return render(request, "accounts/profile_update.html", context)
