from django.conf.urls import url
from RevisionLinks import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^gcse/$', views.gcse, name="gcse"),
    url(r'^gcse/(?P<subject_name>\w+)/', views.GCSESubject, name="gcsesubject"),
]
