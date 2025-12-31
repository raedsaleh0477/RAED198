from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="المستخدم"
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="رقم الهاتف"
    )
    city = models.CharField(
        max_length=100,
        verbose_name="المدينة"
    )
    address = models.TextField(
        verbose_name="العنوان"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء"
    )

    def __str__(self):
        return self.user.username
