from rest_framework import serializers

from post.models import News, Article


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "image", "created_at", "updated_at")


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "image", "created_at", "updated_at")
