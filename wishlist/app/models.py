from django.db import models

"""модель подарка или желания"""


class Item(models.Model):
    title = models.CharField('Название хотелки', max_length=300)
    description = models.CharField('Подробное описание', max_length=500)
    price = models.IntegerField()
    is_complete = models.BooleanField('Закрыто', default=False)

    class Meta:
        verbose_name = 'Желание'
        verbose_name_plural = ('Желания')

    def __str__(self):
        return self.title
