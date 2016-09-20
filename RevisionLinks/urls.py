from django.conf.urls import url
from RevisionLinks import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^gcse/$', views.gcse, name="gcse"),
    url(r'^alevel/$', views.alevel, name="alevel"),
    url(r'^alevel/(?P<subject_name>[\w+.])/', views.ALevelSubject, name="alevelsubject"),
    url(r'^gcse/(?P<subject_name>[\w+.])/', views.GCSESubject, name="gcsesubject"),
]
