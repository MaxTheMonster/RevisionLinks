from django.shortcuts import render, render_to_response
from .models import Subject, Resource
from django.template import RequestContext
from django.db import connection


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


def index(request):
    return render(request, "RevisionLinks/index.html")


def gcse(request):
    subjects = Subject.objects.all().order_by("name")
    print("YO")
    return render(request, "RevisionLinks/gcse.html", {"subjects": subjects})

def GCSESubject(request, subject_name):
    subject_name = subject_name.title()
    subject = Subject.objects.filter(name=subject_name)
    print(subject)
    if subject:
        print("Success")
        error = ""
        print(subject_name)
        website_resources = Resource.objects.filter(subject__name=subject_name, type=1).exclude(exam__name=1)
        video_resources = Resource.objects.filter(subject__name=subject_name, type=2).exclude(exam__name=1)
        book_resources = Resource.objects.filter(subject__name=subject_name, type=3).exclude(exam__name=1)
        resources = Resource.objects.filter(subject__name=subject_name).exclude(exam__name=1)
        if not resources:
            error = "Could not find any resources for GCSE " + subject_name
        else:
            print(resources)
        return render(request, "RevisionLinks/gcsesubject.html", {"resources": resources, "subject": subject_name, "error": error, "video_resources": video_resources, "website_resources": website_resources, "book_resources": book_resources})

    else:
        print("Wow")
        return render(request, "RevisionLinks/404.html")


def gcsePastPapers(request, subject_name):
    return render(request, "RevisionLinks/gcsepastpapers.html", {"subjects": subjects})
