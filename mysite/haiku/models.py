from django.db import models

# Create your models here.
class Kigo(models.Model):
  SEASON_CHOICES = [
    ("spring", "春"),
    ("summer", "夏"),
    ("autumn", "秋"),
    ("winter", "冬"),
  ]

  GENRE_CHOICES = [
    ("plant", "植物"),
    ("animal", "動物"),
    ("event", "行事"),
    ("weather", "気象"),
  ]

  word = models.CharField(max_length=20, verbose_name="季語")
  season = models.CharField(max_length=6, choices=SEASON_CHOICES, verbose_name="季節")
  genre = models.CharField(max_length=10, choices=GENRE_CHOICES, verbose_name="お題ジャンル")

  def __str__(self):
    return self.word