from rest_framework.generics import ListAPIView
from django.db.models import Min, Max, Count

from common.models import Region, Career
from common.serializers import (
    RegionSerializer,
    CareerSerializer,
    CareerSalaryCountSerializer,
)


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()[:10]
    serializer_class = RegionSerializer


class CareerListAPIView(ListAPIView):
    queryset = Career.objects.all()[:10]
    serializer_class = CareerSerializer


class CareerInRegionListAPIView(ListAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

    def get_queryset(self):
        region = self.kwargs.get("region")
        return self.queryset.filter(region__title__icontains=region)


class CareerSalaryCountListAPIView(ListAPIView):
    queryset = (
        Career.objects.all()
        .prefetch_related("jobs")
        .annotate(
            price_min=Min("jobs__price_from"),
            price_max=Max("jobs__price_to"),
            jobs_count=Count("jobs"),
        )
    )
    serializer_class = CareerSalaryCountSerializer
