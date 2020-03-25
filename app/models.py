from django.db import models

gen = (
    ('Male','Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

# Create your models here.
class Visitor(models.Model):
    fio = models.CharField(
        max_length = 30
        )

    num = models.CharField(
        max_length = 8
    )

    birthday = models.DateField(
    )

    gender = models.CharField(
        max_length = 6,
        choices = gen
    )

    def __str__(self):
        return self.fio

class Usage(models.Model):
    visitor = models.ForeignKey(
        Visitor,
        on_delete = models.CASCADE
        )
    date_on = models.DateField(

    )

    date_of = models.DateField(

    )

    book_name = models.CharField(
        max_length = 30
    )

    book_id = models.CharField(
        max_length = 8
    )

    book_author = models.CharField(
        max_length = 30
    )

