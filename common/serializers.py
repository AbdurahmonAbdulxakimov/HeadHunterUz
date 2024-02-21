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


class CareerSalaryCountSerializer(serializers.ModelSerializer):
    price_min = serializers.IntegerField()
    price_max = serializers.IntegerField()
    jobs_count = serializers.IntegerField()

    class Meta:
        model = Career
        fields = (
            "id",
            "title",
            "price_min",
            "price_max",
            "jobs_count",
        )
