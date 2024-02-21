from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from company.views import CompanyInRegionAPIView

from users.api.views import UserViewSet
from job.views import JobShortListAPIView, JobsInRegionAPIView
from post.views import NewsListAPIView, ArticleListAPIView
from common.views import RegionListAPIView, CareerListAPIView, CareerInRegionListAPIView


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"

urlpatterns = [
    # Main page routes
    path("main/jobs/", JobShortListAPIView.as_view()),
    path("main/jobs/<str:region>/", JobsInRegionAPIView.as_view()),
    #
    path("main/news/", NewsListAPIView.as_view()),
    path("main/articles/", ArticleListAPIView.as_view()),
    #
    path("main/regions/", RegionListAPIView.as_view()),
    #
    path("main/careers/", CareerListAPIView.as_view()),
    path("main/careers/<str:region>/", CareerInRegionListAPIView.as_view()),
    path("main/company/<str:region>/", CompanyInRegionAPIView.as_view()),
]
urlpatterns += router.urls
