from rest_framework import serializers

from job.models import Job, Experience
from common.serializers import CareerSerializer, RegionSerializer


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            "id",
            "title",
            "code",
        )


class JobShortSerializer(serializers.ModelSerializer):
    career = CareerSerializer()
    region = RegionSerializer()
    company = serializers.StringRelatedField(source="company.title", read_only=True)

    class Meta:
        model = Job
        fields = (
            "id",
            "title",
            "career",
            "region",
            "company",
            "price_from",
            "price_to",
            "created_at",
            "updated_at",
        )


class JobSerializer(serializers.ModelSerializer):
    experience = ExperienceSerializer()
    company = serializers.StringRelatedField(source="company.title", read_only=True)
    career = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Job
        fields = (
            "id",
            "title",
            "description",
            "region",
            "experience",
            "employment",
            "career",
            "replies",
            "price_from",
            "price_to",
            "company",
            "created_at",
            "updated_at",
            "updated_at",
        )
