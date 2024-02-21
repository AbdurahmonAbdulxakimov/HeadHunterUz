from django.db import models

from utils.models import BaseModel


class Region(BaseModel):
    title = models.CharField(max_length=256)
    neighbors = models.ManyToManyField("self", null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class Career(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.title
