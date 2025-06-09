from django.db import models
from django.conf import settings

class CommonNameModelMixin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    name = models.CharField('Название', max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
