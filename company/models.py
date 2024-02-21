from django.db import models

from utils.models import BaseModel
from common.models import Career


class Company(BaseModel):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="companies/", null=True, blank=True)

    career = models.ForeignKey(
        Career, on_delete=models.CASCADE, related_name="companies"
    )

    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
