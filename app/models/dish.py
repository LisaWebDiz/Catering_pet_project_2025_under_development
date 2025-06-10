from django.db import models

from app.mixins.model_mixins import CommonNameModelMixin


class Dish(CommonNameModelMixin):

    class PRESENTATION(models.TextChoices):
        DELICATESSEN = ('delicatessen', 'Холодные закуски')
        HOT_APPETIZERS = ('hot_appetizers', 'Горячие закуски')
        FIRST_COURSE = ('first course', 'Первое блюдо: суп')
        MAIN_DISH = ('main_dish', 'Горячее')
        DESSERT = ('dessert', 'Десерт')
        BEVERAGES = ('beverages', 'Напитки')
        OTHER = ('other', 'Иное')

    recipe = models.CharField('Рецепт', max_length=5000, blank=True)
    products = models.ManyToManyField('Product', through='DishProduct',  blank=True, related_name='products_dishes')
    cooking_tools = models.ManyToManyField('CookingTool', related_name='tools_dishes', blank=True,
                                           verbose_name='Кухонные инструменты')
    presentation = models.CharField('Подача блюда', choices=PRESENTATION.choices,
                                    default=PRESENTATION.DELICATESSEN, max_length=35)
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