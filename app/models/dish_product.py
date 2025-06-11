from decimal import Decimal

from django.conf import settings
from django.db import models

from app.models import Dish, Product, Unit


class DishProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='Блюдо')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name='Единица измерения')
    amount = models.DecimalField('Количество', max_digits=10, decimal_places=2, default=Decimal('0.00'))

    class Meta:
        verbose_name = 'Продукт для блюда'
        verbose_name_plural = 'Продукты для блюда'
        ordering = ['dish']

    def __str__(self):
        return f'{self.product} - {self.amount} {self.unit} для {self.dish}'
