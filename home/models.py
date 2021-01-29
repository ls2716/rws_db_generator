from django.db import models
from django.db.models.deletion import CASCADE

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)





class BaseMeaning(models.Model):
    global_id = models.CharField(max_length=50)
    part_of_speech = models.CharField(max_length=50)
    text = models.CharField(max_length=400)

    def __str__(self) -> str:
        return self.global_id

class Word(models.Model):
    basemeaning = models.ForeignKey(BaseMeaning, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    labels = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.word