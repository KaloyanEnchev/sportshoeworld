from rest_framework import serializers
from .models import Shoe
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = "__all__"


class ShoeNestedReadSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Shoe
        fields = "__all__"