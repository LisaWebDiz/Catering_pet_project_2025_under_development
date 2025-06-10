from django.db import models

from app.mixins.model_mixins import CommonNameModelMixin


class Unit(CommonNameModelMixin):

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_unit_name')
        ]
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'
        ordering = ['name']

    def __str__(self):
        return self.name