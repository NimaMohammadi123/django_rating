from rest_framework import serializers
from blog.models import Post ,Rating

class ListApiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ="__all__"

class DetailApiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ="__all__"

class RatingApiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields ="__all__"