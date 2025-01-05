from django.db import models


class User(models.Model):
    email = models.EmailField()
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)


class Coords(models.Model):
    latitude = models.FloatField(max_length=50, verbose_name="Широта")
    longitude = models.FloatField(max_length=50, verbose_name="Долгота")
    height = models.IntegerField(verbose_name="Высота")


class Level(models.Model):

    winter = models.CharField(max_length=20, verbose_name='Зима', blank=True, null=True)
    summer = models.CharField(max_length=20, verbose_name='Лето', blank=True, null=True)
    autumn = models.CharField(max_length=20, verbose_name='Осень', blank=True, null=True)
    spring = models.CharField(max_length=20, verbose_name='Весна', blank=True, null=True)


class Pereval(models.Model):
    new = "new"
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    STATUS = [
        (new, "новый"),
        (pending, "модератор взял в работу"),
        (accepted, "модерация прошла успешно"),
        (rejected, "модерация прошла, информация не принята"),
    ]

    title = models.CharField(max_length=50)
    other_title = models.CharField(max_length=50)
    connect = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default=new)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)


class Images(models.Model):
    data = models.URLField()
    title = models.CharField(max_length=50)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')
