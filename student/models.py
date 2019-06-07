from django.db import models


class Student(models.Model):
    name = models.CharField("name", max_length=50)
    birthdate = models.DateField("birthdate")

    def __str__(self):
        return "{} {}".format(self.name, self.birthdate)

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"
