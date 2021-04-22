from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256, null=True)
    shortDescription = models.CharField(max_length=256, null=True)
    longDescription = models.TextField(null=True)

    def __str__(self):
        return f"{self.id} {self.title}"


class Review(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    book_id = models.BigIntegerField(default=1)
