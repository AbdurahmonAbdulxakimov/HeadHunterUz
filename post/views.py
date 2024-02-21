from rest_framework.generics import ListAPIView

from post.models import News, Article
from post.serializers import NewsSerializer, ArticleSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all().order_by("-updated_at")[:4]
    serializer_class = NewsSerializer


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all().order_by("-updated_at")[:4]
    serializer_class = ArticleSerializer
