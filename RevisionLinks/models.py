from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=140, unique=True)
    color = models.ForeignKey(Color)

    def __str__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField(default=2, max_length=10, unique=True)

    def __str__(self):
        return self.name


class ExamBoard(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=140)
    url = models.URLField()
    description = models.CharField(max_length=140)
    exam = models.ForeignKey(Exam)
    type = models.ForeignKey(Type)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_added = models.DateTimeField('Date Added')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class PastPaper(models.Model):
    name = models.CharField(max_length=140)
    url = models.URLField()
    exam_board = models.ForeignKey(ExamBoard)
    subject = models.ForeignKey(Subject)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
