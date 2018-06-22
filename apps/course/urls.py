from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="main_page"),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy, name="my_destroy"),
    url(r'^courses/process_delete/(?P<id>\d+)$', views.process_destroy, name="my_process_destroy"),
    url(r'^courses/create$', views.create, name="my_create")
]