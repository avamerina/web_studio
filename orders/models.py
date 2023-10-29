from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from utils.helpers import generate_order_number


class Order(models.Model):
    NOT_CHECKED = "NOT_CHECKED"
    TO_PROCESS = "TO_PROCESS"
    PROCESSED = "PROCESSED"
    STATUSES = [
        (NOT_CHECKED, "Не проверен"),
        (TO_PROCESS, "В обработку"),
        (PROCESSED, "Обработан")
    ]
    description = models.CharField(max_length=300, default='')
    slug = models.SlugField(primary_key=True, blank=True, unique=True,  max_length=6)
    status = models.CharField(max_length=100, choices=STATUSES, default=NOT_CHECKED)
    user = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.slug:
            while True:
                generated_number = generate_order_number()
                if not Order.objects.filter(slug=generated_number):
                    self.slug = slugify(generated_number)
        return super().save(*args, **kwargs)


class File(models.Model):
    url = models.CharField(max_length=2000)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


