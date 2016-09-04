import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Revision.settings")
import django
django.setup()
from RevisionLinks.models import Subject, Exam

def populate():
    exams = [0, 1, 2]
    subjects = ["Maths", "English", "Biology", "Physics", "Chemistry", "Computing"]

    for exam in exams:
        e = Exam(name=exam)
        e.save()

    for subject in subjects:
        s = Subject(name=subject)
        s.save()

populate()
