from django.db import models

from utils.models import BaseModel


class News(BaseModel):
    image = models.ImageField(upload_to="news/")
    title = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.title


class Article(BaseModel):
    image = models.ImageField(upload_to="news/")
    title = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.title
