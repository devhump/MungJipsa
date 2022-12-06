from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("dogsignup/", views.dogsignup, name="dogsignup"),
    path("dogprofile/<int:dog_pk>/", views.dogprofile, name="dogprofile"),
    path("dogupdate/<int:dog_pk>/", views.dogupdate, name="dogupdate"),
    path("dogdelete/", views.dogdelete, name="dogdelete"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("password/", views.password, name="password"),
    path("delete/", views.delete, name="delete"),
    path("follow/<username>/", views.follow, name="follow"),
    path("profile/<username>/", views.profile, name="profile"),
    path("update/<int:pk>/", views.update, name="update"),
    path("follow/<username>/", views.follow, name="follow"),
    path("", views.index, name="index"),
]
