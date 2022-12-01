from django.db import models
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

# 이미지


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="post"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


def get_image_filename(instance, filename):
    # 해당 Post 모델의 title 을 가져옴
    title = instance.review.title
    # slug - 의미있는 url 사용을 위한 필드.
    # slugfy 를 사용해서 title을 slug 시켜줌.
    slug = slugify(title)
    # 제목 - 슬러그된 파일이름 형태
    return "reviews/images/%s-%s" % (slug, filename)


class Images(models.Model):
    # default = None 으로 이미지를 등록하지 않을 때는 db에 저장되지 않음.
    review = models.ForeignKey(
        Review, default=None, on_delete=models.CASCADE, related_name="image"
    )
    # get_image_filename method 경로 사용
    # 문자열로 경로를 지정할 경우, media/문자열 지정 경로로 저장되며, 중간 디렉토리 경로를 지정할 수 있고,
    # 메소드(함수)로 지정할 경우, 중간 디렉토리 경로명뿐만 아니라 파일명까지 지정 가능
    image = ProcessedImageField(upload_to=get_image_filename, blank=True, null=True)

    # admin 에서 모델이름
    class Meta:
        # 단수
        verbose_name = "Image"
        # 복수
        verbose_name_plural = "Images"

    # 이것도 역시 post title 로 반환
    def __str__(self):
        return str(self.post)
