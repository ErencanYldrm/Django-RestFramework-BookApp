from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Book(models.Model):
    writer = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books")
    name = models.CharField(max_length=200)
    releaseDate = models.DateField()
    numberOfPage = models.IntegerField()
