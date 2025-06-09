from django.db import models

from app.mixins.model_mixins import CommonNameModelMixin


class Dish(CommonNameModelMixin):
    recipe = models.CharField('Рецепт', max_length=5000, blank=True)
    min_portioning = models.PositiveIntegerField('Минимальная порционность')


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_dish_name')
        ]
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['name']

    def __str__(self):
        return self.name