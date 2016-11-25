from django.conf.urls import url
from . import views


urlpatterns = [
   
    url(r'^delete/(?P<id>(\d+))/(?P<verification>(\w+))$', views.delete),
    url(r'^delete_course/(?P<id>\d+)$', views.delete_course),
    url(r'^add_course?$', views.add_course),
    url(r'^$', views.index),
]
