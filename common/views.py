from rest_framework.generics import ListAPIView

from common.models import Region, Career
from common.serializers import RegionSerializer, CareerSerializer


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
