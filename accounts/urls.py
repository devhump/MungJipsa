from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("dogsignup/", views.dogsignup, name="dogsignup"),
    path("dogupdate/", views.dogupdate, name="dogupdate"),
    path("dogdelete/", views.dogdelete, name="dogdelete"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("password/", views.password, name="password"),
    path("delete/", views.delete, name="delete"),
    path("follow/<username>/", views.follow, name="follow"),
    path("profile/<username>/", views.profile, name="profile"),
    path("update/<int:pk>/", views.update, name="update"),
    path("follow/<username>/", views.follow, name="follow"),
    # path("dogprofile/<name>/",views.dogprofile, name="dogprofile"),
    path("", views.index, name="index"),
    path("callback/", views.callback, name="callback"),
]
