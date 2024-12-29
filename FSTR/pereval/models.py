from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    fam = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    otc = models.CharField(max_length=20)
    phone = models.CharField()


class Coords(models.Model):
    latitude = models.FloatField(max_length=50, verbose_name="Широта")
    longitude = models.FloatField(max_length=50, verbose_name="Долгота")
    height = models.IntegerField(verbose_name="Высота")


class Level(models.Model):
    easy = 'easy'
    average = 'aver'
    hard = 'hard'

    the_difficulty = [
        (easy, "Легкая сложность"),
        (average, "Средняя сложность"),
        (hard, "Тяжелая сложность"),
    ]

    winter = models.CharField(max_length=4, choices=the_difficulty, default=average)
    summer = models.CharField(max_length=4, choices=the_difficulty, default=average)
    autumn = models.CharField(max_length=4, choices=the_difficulty, default=average)
    spring = models.CharField(max_length=4, choices=the_difficulty, default=average)


class Pereval(models.Model):
    title = models.CharField(max_length=50)
    other_title = models.CharField()
    connect = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


class Images(models.Model):
    data = models.URLField()
    title = models.CharField()
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)
