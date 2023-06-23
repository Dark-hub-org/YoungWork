from django.db import models


class YourModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

    # Добавьте остальные поля вашей модели

    def str(self):
        return self.field1  # Верните строковое представление объекта

    class Meta:
        verbose_name_plural = "Your Models"  # Название таблицы во
