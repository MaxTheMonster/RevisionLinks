from django.contrib import admin
from RevisionLinks.models import Subject, Resource, Color, Type, ExamBoard, PastPaper

admin.site.register(Subject)
admin.site.register(Color)
admin.site.register(Resource)
admin.site.register(Type)
admin.site.register(ExamBoard)
admin.site.register(PastPaper)
