from rest_framework import serializers

from job.models import Job, Experience, Skill
from common.serializers import CareerSerializer, RegionSerializer
from company.serializers import CompanySimpleSerializer


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            "id",
            "title",
            "code",
        )


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = (
            "id",
            "title",
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
    # company = serializers.StringRelatedField(source="company.title", read_only=True)
    company = CompanySimpleSerializer()
    region = RegionSerializer()
    career = serializers.SlugRelatedField(slug_field="title", read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

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
            "skills",
            "created_at",
            "updated_at",
            "updated_at",
        )
