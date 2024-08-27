from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Product Name"))
    description = models.TextField(verbose_name=_("Description"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    stock = models.PositiveIntegerField(verbose_name=_("Stock Quantity"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name