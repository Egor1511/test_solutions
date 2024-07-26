from django.db import models


class Ad(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок объявления',
    )
    ad_id = models.IntegerField(
        verbose_name='ID объявления',
        unique=True
    )
    author = models.CharField(
        max_length=255,
        verbose_name='Автор объявления',
    )
    views = models.IntegerField(
        verbose_name='Количество просмотров',
        default=0,
    )
    position = models.IntegerField(
        verbose_name='Позиция объявления',
        default=0,
    )

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title
