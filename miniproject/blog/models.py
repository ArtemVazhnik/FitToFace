from django.db import models


# Create your models here.


class Shape(models.Model):
    shape = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.shape#f'Shape {self.pk}'


class Glasses(models.Model):
    type = models.CharField(
        max_length=50,
    )
    photo = models.ImageField(

    )

    shape = models.ManyToManyField(
        Shape,
    )

    def __str__(self):
        return self.type#f'Glasses {self.pk}'


class UserPhoto(models.Model):
    image = models.ImageField(
        upload_to='images'
    )

    shape = models.ForeignKey(
        Shape,
        on_delete=models.CASCADE,
        default='',
        null=True,
    )

    glasses = models.ManyToManyField(
        Glasses,
        null=True,
    )

    def __str__(self):
        return f'UserPhoto {self.pk}'
