from django.urls import path,re_path

from . import views

urlpatterns = [
   # path('',views.sh,name='sh'),
    path('', views.home, name='home'),
    re_path(r'^(?P<items_id>[0-9]+)/$',views.show, name='show'),
]