from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.db.models import Q

from job.serializers import JobSerializer, JobShortSerializer
from job.models import Job


# class JobShortListAPIView(ListAPIView):
#     queryset = Job.objects.select_related("company", "region", "career").all()
#     serializer_class = JobShortSerializer


class JobsInRegionAPIView(ListAPIView):
    queryset = Job.objects.select_related("company", "region", "career")
    serializer_class = JobShortSerializer

    def get_queryset(self) -> QuerySet:
        region = self.kwargs.get("region")
        qs = super().get_queryset().filter(region__title__icontains=region)

        return qs


class JobRetrieveAPIView(RetrieveAPIView):
    queryset = Job.objects.select_related(
        "company", "region", "career"
    ).prefetch_related("skills")
    serializer_class = JobSerializer


class JobSimilarsListAPIView(ListAPIView):
    queryset = Job.objects.select_related(
        "company", "region", "career"
    ).prefetch_related("skills")
    serializer_class = JobSerializer

    def get_queryset(self) -> QuerySet:
        job = Job.objects.get(id=self.kwargs["job_id"])
        qs = (
            super()
            .get_queryset()
            .filter(Q(career__title=job.career.title))
            .exclude(id=job.id)
        )

        return qs


class JobsListAPIView(ListAPIView):
    queryset = Job.objects.select_related(
        "company", "region", "career"
    ).prefetch_related("skills")
    serializer_class = JobSerializer
