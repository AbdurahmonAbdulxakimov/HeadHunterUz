from rest_framework import serializers

from common.models import Career, Region


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = (
            "id",
            "title",
        )


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = (
            "id",
            "title",
        )
