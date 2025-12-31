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

    class Meta:
        verbose_name = "عميل"
        verbose_name_plural = "العملاء"
        ordering = ['-created_at']

    def __str__(self):
        return f"العميل: {self.user.username}"
