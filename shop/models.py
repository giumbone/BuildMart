from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

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

    def clean(self):
        # Example of custom validation logic
        if self.price <= 0:
            raise ValidationError(_("Price must be greater than 0."))
        if self.stock < 0:
            raise ValidationError(_("Stock quantity cannot be negative."))

    def save(self, *args, **kwargs):
        try:
            # This ensures all Django model field validations are checked before saving
            self.full_clean()
            # Wrap save operation in a transaction to ensure database integrity
            with transaction.atomic():
                super(Product, self).save(*args, **kwargs)
        except ValidationError as e:
            # Handle specific validation errors here or pass up to be handled at a higher level
            raise e
        except Exception as e:
            # Log this exception or handle it as per your error handling policy
            raise ValueError("An error occurred saving the product. Please try again.")