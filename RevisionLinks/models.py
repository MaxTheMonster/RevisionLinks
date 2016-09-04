from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=140, unique=True)

    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(default=3, max_length=10, unique=True)

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=140, unique=True)
    url = models.URLField()
    description = models.CharField(max_length=140)
    exam = models.ForeignKey(Exam)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_added = models.DateTimeField('Date Added')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
