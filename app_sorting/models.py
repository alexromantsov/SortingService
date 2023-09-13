from django.db import models
from django.core.exceptions import ValidationError


class SortingFunction(models.Model):
    module_name = models.CharField(
        verbose_name="Имя модуля",
        max_length=100
    )
    function_name = models.CharField(
        verbose_name="Имя функции",
        max_length=100
    )
    description = models.TextField(
        verbose_name="Описание функции"
    )

    class Meta:
        db_table = "table_function"
        verbose_name = "Функция"
        verbose_name_plural = "Таблица функций"

    def __str__(self):
        return f"{self.module_name} - {self.function_name}"

    def clean(self):
        if not self.module_name or not self.function_name:
            raise ValidationError("Имя модуля и имя функции не должны быть пустыми.")
