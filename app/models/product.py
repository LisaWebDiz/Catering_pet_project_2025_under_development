from django.db import models

from app.mixins.model_mixins import CommonNameModelMixin


class Product(CommonNameModelMixin):


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_product_name')
        ]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

    def __str__(self):
        return self.name