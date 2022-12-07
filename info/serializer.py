from rest_framework import serializers
from .models import PetPlace, PetPlaceSlideImage


class PlaceSlideImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = PetPlaceSlideImage
        fields = ["slideimage"]


class PlaceSerializer(serializers.ModelSerializer):

    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = obj.petplaceslideimage_set.all()
        return PlaceSlideImageSerializer(instance=image, many=True).data

    class Meta:
        model = PetPlace
        fields = ["id", "name", "address", "tel", "url", "images"]

    def create(self, validated_data):
        instance = PetPlace.objects.create(**validated_data)
        image_set = self.context["request"].FILES
        for image_data in image_set.getlist("image"):
            PetPlaceSlideImage.objects.create(place=instance, image=image_data)
        return instance
