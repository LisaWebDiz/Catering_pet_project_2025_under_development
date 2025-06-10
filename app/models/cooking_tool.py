from django.db import models

from app.mixins.model_mixins import CommonNameModelMixin


class CookingTool(CommonNameModelMixin):
    comment = models.CharField('Комментарий', max_length=150, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_tool_name')
        ]
        verbose_name = 'Кухонный инструмент'
        verbose_name_plural = 'Кухонные инструменты'
        ordering = ['name']

    def __str__(self):
        return self.name