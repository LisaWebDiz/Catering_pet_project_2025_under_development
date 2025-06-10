from decimal import Decimal

from django.db import models

from app.mixins.model_mixins import CommonNameModelMixin
from app.models import Dish, Product, Unit


class DishProduct(CommonNameModelMixin):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='Блюдо')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name='Единица измерения')
    amount = models.DecimalField('Количество', max_digits=10, decimal_places=2, default=Decimal('0.00'))


    def __str__(self):
        return f'{self.product} - {self.amount} {self.unit} для {self.dish}'
