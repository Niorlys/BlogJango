from django.db import models
from django.utils import timezone


class Tags(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class BlogEntry(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    tags = models.ManyToManyField(Tags)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-published_at"]
        indexes = [
            models.Index(fields=["-publish_at"]),
        ]

    def __str__(self) -> str:
        return self.title
