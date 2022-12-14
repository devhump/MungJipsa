from django.urls import path
from . import views
from .views import SearchFormView


# Create your views here.

app_name = "reviews"
urlpatterns = [
    # 멍스타그렘
    path("", views.index, name="index"),
    # 리뷰작성
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    # 리뷰 수정
    path("<int:pk>/update/", views.update, name="update"),
    # 리뷰 수정
    path("<int:pk>/update/", views.update, name="update"),
    # 리뷰 삭제
    path("<int:pk>/delete/", views.delete, name="delete"),
    # 댓글 작성
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    # 댓글 삭제
    path(
        "<int:pk>/comments/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    # 리뷰 글 좋아요
    path("<int:pk>/like/", views.like, name="like"),
    # 검색
    path("search/", views.SearchFormView.as_view(), name="search"),
    # 댓글 좋아요
    path("<int:pk>/<int:comment_pk>/likes/", views.likes, name="likes"),
    path("follow/<int:pk>/", views.follow, name="follow"),
    path("follows/", views.follows, name="follows"),
]
