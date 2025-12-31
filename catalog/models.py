from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="اسم التصنيف"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="نشط"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء"
    )

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="التصنيف"
    )
    name = models.CharField(
        max_length=200,
        verbose_name="اسم المنتج"
    )
    description = models.TextField(
        blank=True,
        verbose_name="الوصف"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="السعر"
    )
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name="الكمية المتوفرة"
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name="متاح"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
        ordering = ['-created_at']

    def __str__(self):
        return self.name
