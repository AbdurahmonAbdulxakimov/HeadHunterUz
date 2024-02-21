from rest_framework import serializers

from company.models import Company


class CompanySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            "id",
            "title",
            "image",
        )


class CompanySerializer(serializers.ModelSerializer):
    jobs_count = serializers.IntegerField()

    class Meta:
        model = Company
        fields = (
            "id",
            "title",
            "image",
            "career",
            "is_verified",
            "jobs_count",
            "created_at",
            "updated_at",
        )
