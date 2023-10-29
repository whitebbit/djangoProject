from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    phone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    subject = models.CharField(max_length=100, null=True, default="Unknown")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Group(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
