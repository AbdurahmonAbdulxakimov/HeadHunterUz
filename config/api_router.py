from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from company.views import CompanyInRegionAPIView

from users.api.views import UserViewSet
from job.views import (
    JobShortListAPIView,
    JobsInRegionAPIView,
    JobRetrieveAPIView,
    JobSimilarsListAPIView,
)
from post.views import NewsListAPIView, ArticleListAPIView
from common.views import (
    RegionListAPIView,
    CareerListAPIView,
    CareerInRegionListAPIView,
    CareerSalaryCountListAPIView,
)


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"

urlpatterns = [
    # Main page routes
    # path("main/jobs/", JobShortListAPIView.as_view()),
    path("main/jobs/", CareerSalaryCountListAPIView.as_view()),
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
    # Job pages
    path("jobs/<int:pk>/", JobRetrieveAPIView.as_view()),
    path("jobs/similar/<int:job_id>/", JobSimilarsListAPIView.as_view()),
]
urlpatterns += router.urls
