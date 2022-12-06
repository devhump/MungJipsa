from rest_framework import serializers
from .models import PetPlace, PetPlaceSlideImage, PetPlaceBodyImage


class PlaceSlideImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = PetPlaceSlideImage
        fields = ["slideimage"]


class PlaceBodyImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = PetPlaceBodyImage
        fields = ["bodyimage"]
