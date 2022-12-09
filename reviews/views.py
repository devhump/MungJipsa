from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.core.paginator import Paginator
from reviews.forms import ReviewForm, CommentForm, ImageForm, PostSearchForm
from .models import Review, Comment, Images
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.db.models import Q
import random

# 멍스타그렘
def index(request):
    reviews = Review.objects.all().order_by("-created_at")
    search = request.GET.get("search")
    if search:
        reviews = reviews.filter(
            Q(title__icontains=search) | Q(content__icontains=search)
        )

    comment_form = CommentForm()
    page = request.GET.get("page", "1")
    paginator = Paginator(reviews, 6)
    posts = paginator.get_page(page)
    num = random.randrange(1, 9)
    lst = [
        "01.png",
        "02.png",
        "03.png",
        "04.png",
        "05.png",
        "06.jpg",
        "07.jpg",
        "08.jpg",
    ]
    hospital = lst[num - 1]
    sub = "../../static/images/" + hospital
    num2 = random.randrange(1, 6)
    lst2 = ["D1.png", "D2.png", "D3.png", "D4.png", "D5.png"]
    photo = lst2[num2 - 1]
    address = "../../static/images/" + photo

    context = {
        "posts": posts,
        "reviews": reviews,
        "comment_form": comment_form,
        "search": search,
        "aside": sub,
        "aside2": address,
    }
    return render(request, "reviews/index.html", context)


# 멍스타그렘 글 작성
@login_required
def create(request):
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=4)

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        formset = ImageFormSet(
            request.POST, request.FILES, queryset=Images.objects.none()
        )
        print("1")

        if review_form.is_valid() and formset.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            print("2")
            for form in formset.cleaned_data:

                if form:
                    # image file
                    image = form["image"]
                    print(form)
                    print(form["image"])
                    # post, image file save
                    photo = Images(review=review, image=image)
                    photo.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()
        formset = ImageFormSet(queryset=Images.objects.none())

    context = {
        "review_form": review_form,
        "formset": formset,
    }
    return render(request, "reviews/form.html", context)


def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)

    comment_form = CommentForm()
    # template에 객체 전달
    context = {
        "review": review,
        "comments": review.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "reviews/detail.html", context)


# 리뷰 삭제


def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review.delete()
        return redirect("reviews:index")
    context = {"review": review}
    return render(request, "reviews/detail.html", context)


# 리뷰 수정


def update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user == review.user:
        if request.method == "POST":
            # POST : input 값 가져와서, 검증하고, DB에 저장
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
                review_form.save()
                return redirect("reviews:detail", review.pk)
            # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 review_form을 랜더링
        else:
            # GET : Form을 제공
            review_form = ReviewForm(instance=review)
        context = {
            "review_form": review_form,
        }
        return render(request, "reviews/form.html", context)
    else:
        return redirect("reviews:detail", review.pk)


# 댓글 작성하기


def comment_create(request, pk):

    review = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()

    return redirect("reviews:index")


# 댓글 지우기


def comment_delete(request, comment_pk, pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user.is_authenticated and request.user == comment.user:
        comment.delete()
        return redirect("reviews:detail", pk)


def like(request, pk):
    review = get_object_or_404(Review, pk=pk)
    # print('hi') 요청 확인 위함
    # 만약 로그인한 유저(request.user)가 이 글을 좋아요 눌렀다면,

    if request.user in review.like_users.all():

        # 좋아요 삭제하고
        review.like_users.remove(request.user)
        is_liked = False
    else:  # 좋아요 누르지 않은 상태라면 좋아요에 추가하고
        review.like_users.add(request.user)
        is_liked = True
        # 상세 페이지로 redirect
    context = {"is_liked": is_liked, "likeCount": review.like_users.count()}
    return JsonResponse(context)


# 검색
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = "reviews/search.html"

    def form_valid(self, form):
        searchWord = form.cleaned_data["search_word"]
        post_list = Review.objects.filter(
            Q(title__icontains=searchWord) | Q(content__icontains=searchWord)
        ).distinct()

        context = {}
        context["form"] = form
        context["search_term"] = searchWord
        context["object_list"] = post_list

        return render(self.request, self.template_name, context)


# 댓글 좋아요
def likes(request, pk, comment_pk):
    review = Review.objects.get(pk=pk)
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user in comment.like_users.all():
            comment.like_users.remove(request.user)
            is_liked = False

            comment.user.save()

        else:
            comment.like_users.add(request.user)
            is_liked = True

            comment.user.save()
        context = {
            "is_liked": is_liked,
            "likeCount": comment.like_users.count(),
        }
        return JsonResponse(context)


#
