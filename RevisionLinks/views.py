from django.shortcuts import render
from .models import Subject, Resource
from django.http import Http404
from django.db import connection


def index(request):
    return render(request, "RevisionLinks/index.html")

def gcse(request):
    subjects = Subject.objects.all().order_by("name")
    print("YO")
    return render(request, "RevisionLinks/gcse.html", {"subjects": subjects})

def alevel(request):
    subjects = Subject.objects.all().order_by("name")
    return render(request, "RevisionLinks/alevel.html", {"subjects": subjects})

def GCSESubject(request, subject_name):
    subject_name = subject_name.title()
    subject = Subject.objects.filter(name=subject_name)
    print(subject)
    if subject:
        print("Success")
        error = ""
        print(subject_name)
        resources = Resource.objects.filter(subject__name=subject_name).exclude(exam__name=1)
        if not resources:
            error = "Could not find any resources for GCSE " + subject_name
        else:
            print(resources)
        return render(request, "RevisionLinks/gcsesubject.html", {"resources": resources, "subject": subject_name, "error": error})

    else:
        print("Wow")
        return render(request, "RevisionLinks/404.html")

def ALevelSubject(request, subject_name):
    subject_name = subject_name.title()
    error = ""
    print(subject_name)
    resources = Resource.objects.filter(subject__name=subject_name).exclude(exam=0)
    if not resources:
        error = "Could not find any resources for A-Level " + subject_name
    else:
        print(resources)
    return render(request, "RevisionLinks/alevelsubject.html", {"resources": resources, "subject": subject_name, "error": error})
