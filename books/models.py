from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class Book(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/")
    author = models.CharField(max_length=500)
    owner = models.ForeignKey(get_user_model(), models.CASCADE, related_name="user_book")
    duration = models.DurationField()
    lent = models.BooleanField(default=False)

    class AvailableManager(models.Manager):

        def get_queryset(self):
            return super().get_queryset()\
                .filter(lent=False)

    objects = models.Manager()
    available_books = AvailableManager()


class Request(models.Model):

    class Status(models.TextChoices):
        PENDING = "PD", "Pending"
        REJECTED = "RT", 'Rejected'
        APPROVED = "AP", "Approved"

    book_id = models.ForeignKey(Book, models.CASCADE, related_name="book_request")
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PENDING)
    reject_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    approved_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    return_date = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(get_user_model(), models.CASCADE, related_name="user_request")




