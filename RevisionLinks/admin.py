from django.contrib import admin
from RevisionLinks.models import Subject, Resource, Color, Type

admin.site.register(Subject)
admin.site.register(Color)
admin.site.register(Resource)
admin.site.register(Type)
