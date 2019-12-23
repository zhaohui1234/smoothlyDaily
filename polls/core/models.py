from django.db import models

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=100)

class Job(models.Model):
    job_name = models.CharField(max_length=20)

class Record(models.Model):
    name =  models.CharField(max_length=20)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)

