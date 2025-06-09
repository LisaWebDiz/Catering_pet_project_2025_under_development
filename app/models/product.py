from decimal import Decimal

from django.db import models

from app.mixins.model_mixins import CommonNameModelMixin
from app.models import Dish, Unit


class Product(CommonNameModelMixin):
    dish = models.ForeignKey(Dish, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Блюдо',
                             related_name='dish_products')
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Единица измерения', related_name='unit_products')
    amount = models.DecimalField('Количество', max_digits=10, decimal_places=2, default=Decimal('0.00'))


    class Meta:
        # app_label = 'catering'
        constraints = [
            models.UniqueConstraint(fields=['name', 'dish'], name='unique_product_name_per_dish')
        ]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

    def __str__(self):
        return self.name