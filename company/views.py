from rest_framework.generics import ListAPIView
from django.db.models import Count

from company.models import Company
from company.serializers import CompanySerializer


class CompanyInRegionAPIView(ListAPIView):
    queryset = Company.objects.prefetch_related("jobs").all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        region = self.kwargs.get("region")

        return (
            super()
            .get_queryset()
            .annotate(jobs_count=Count("jobs"))
            .filter(jobs__region__title__icontains=region)
        )
