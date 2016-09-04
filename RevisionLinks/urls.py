from django.conf.urls import url
from RevisionLinks import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^gcse/$', views.gcse, name="gcse"),
    url(r'^alevel/$', views.alevel, name="alevel"),
    url(r'^(?P<exam>)/(?P<subject_name>)/$', views.subject, name="subject"),
]
