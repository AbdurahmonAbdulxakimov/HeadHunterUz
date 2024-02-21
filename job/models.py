from django.db import models

from utils.models import BaseModel
from company.models import Company
from common.models import Region, Career


class EmployemntType(models.TextChoices):
    FULL = "Full Time"
    PART = "Part Time"


class Experience(BaseModel):
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.title


class Skill(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.title


class Job(BaseModel):
    title = models.CharField(max_length=256)
    description = models.TextField()

    skills = models.ManyToManyField(Skill, related_name="jobs")

    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    experience = models.ForeignKey(
        Experience, on_delete=models.SET_NULL, blank=True, null=True
    )

    employment = models.CharField(
        max_length=16, choices=EmployemntType.choices, default=EmployemntType.FULL
    )

    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name="jobs")

    replies = models.PositiveIntegerField(default=0)

    price_from = models.PositiveIntegerField(null=True, blank=True)
    price_to = models.PositiveIntegerField(null=True, blank=True)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")

    def __str__(self) -> str:
        return self.title
