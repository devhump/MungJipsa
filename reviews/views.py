from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.core.paginator import Paginator
from reviews.forms import ReviewForm, CommentForm, ImageForm
from .models import Review, Comment, Images, Like
from rest_framework.views import APIView
from rest_framework.response import Response

# 멍스타그렘
def index(request):
    reviews = Review.objects.all()

    comment_form = CommentForm()
    page = request.GET.get("page", "1")
    paginator = Paginator(reviews, 6)
    posts = paginator.get_page(page)

    context = {
        "posts": posts,
        "reviews": reviews,
        "comment_form": comment_form,
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


class ToggleLike(APIView):
    def post(self, request):
        review = request.data.get("review", None)
        favorite_text = request.data.get("favorite_text", True)

        if favorite_text == "favorite_border":
            is_like = True
        else:
            is_like = False
        user = request.session.get("user", None)

        like = Like.objects.filter(review=review, user=user).first()

        if like:
            like.is_like = is_like
            like.save()
        else:
            Like.objects.create(review=review, is_like=is_like, user=user)

        return Response(status=200)
