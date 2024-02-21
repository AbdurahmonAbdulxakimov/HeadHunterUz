from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView

from job.serializers import JobSerializer, JobShortSerializer
from job.models import Job


class JobShortListAPIView(ListAPIView):
    queryset = Job.objects.select_related("company", "region", "career").all()
    serializer_class = JobShortSerializer


class JobsInRegionAPIView(ListAPIView):
    queryset = Job.objects.select_related("company", "region", "career")
    serializer_class = JobShortSerializer

    def get_queryset(self) -> QuerySet:
        region = self.kwargs.get("region")
        qs = super().get_queryset().filter(region__title__icontains=region)

        return qs
