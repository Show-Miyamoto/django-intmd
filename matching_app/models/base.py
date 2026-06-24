from django.db import models
from .base import BaseModel


class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class InheriteModel(BaseModel):