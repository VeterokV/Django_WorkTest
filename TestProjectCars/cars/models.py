from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Car(models.Model):
    make = models.CharField(max_length=20)                                                                              # Марка автомобиля
    carmodel = models.CharField(max_length=50)                                                                          # Модель автомобиля
    year = models.IntegerField(
        validators=[
            MaxValueValidator(3000),
            MinValueValidator(1000)
            ]
        )                                                                                                               # Год выпуска автомобиля с ограниченным промежутком
    desc = models.CharField(max_length=400)                                                                             # Описание автомобиля
    created_at = models.DateTimeField(auto_now_add=True)                                                                # Дата и время создания записи
    updated_at = models.DateTimeField(auto_now=True)                                                                    # Дата и время последнего обновления записи
    id_owner = models.ForeignKey(User, on_delete=models.CASCADE)                                                        # id пользователя, создавшего запись

    def __str__(self):
        return f'{self.make} {self.carmodel} {self.year}'                                                               # Строковое представление объекта


class Comment(models.Model):
    content = models.CharField(max_length=5000)                                                                         # Поле содержания комментария
    created_at = models.DateTimeField(auto_now_add=True)                                                                # Дата и время создания комментария
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)                                                           # id автомобиля
    id_auth = models.ForeignKey(User, on_delete=models.CASCADE)                                                         # id пользователя, написавшего комментарий

    def __str__(self):
        return self.content[:20]
