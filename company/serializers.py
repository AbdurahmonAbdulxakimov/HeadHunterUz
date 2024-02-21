from rest_framework import serializers

from company.models import Company
from job.serializers import JobShortSerializer


class CompanySerializer(serializers.ModelSerializer):
    jobs = JobShortSerializer(many=True, read_only=True)
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
            "jobs",
            "created_at",
            "updated_at",
        )
