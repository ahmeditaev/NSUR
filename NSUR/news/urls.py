from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from .models import News

app_name = 'news'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.mainPage,name='mainPage'),
    url(r'^about/$',views.AboutUs.as_view(),name='aboutUs'),
    url(r'^rukovodstvo/$',views.Rukovodstvo.as_view(),name='rukovodstvo'),
    url(r'^news/$',views.PostListView.as_view(queryset=News.objects.all().order_by('-published')[:20]),name='news'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='details'),
    url(r'emailus/$',views.emailUs,name='emailUs')


]
