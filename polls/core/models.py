from django.db import models

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class Record(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.staff.name + self.job.name
