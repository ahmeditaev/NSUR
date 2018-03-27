from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from .models import News

app_name = 'news'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.mainPage, name='mainPage'),
    url(r'^about/$', views.AboutUs.as_view(), name='aboutUs'),
    url(r'^rukovodstvo/$', views.Rukovodstvo.as_view(), name='rukovodstvo'),
    url(r'^news/', views.postListView, name='news'),
    url(r'^(?P<pk>\d+)/$', views.postDetailsView, name='details'),
    url(r'^emailus/$', views.emailUs, name='emailUs'),
    url(r'^search/',views.search,name='search'),
    url(r'^email/',views.emailUsFooter,name='email')


]
