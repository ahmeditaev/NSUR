from django.shortcuts import render
from django.views import generic
from . import models
from django.utils.timezone import now
from . import forms

# Create your views here.
def mainPage(request):
    posts = models.News.objects.filter(published__lte=now()).order_by('-published')[:9]
    return render(request, 'home.html', {'posts':posts})

class PostListView(generic.ListView):
    model = models.News
    template_name = 'posts/post_list.html'

class PostDetailView(generic.DetailView):
    model = models.News
    template_name = 'posts/post_detail.html'
    context_object_name = 'details'


class AboutUs(generic.ListView):
    template_name = 'tazakoom/aboutus.html'
class Rukovodstvo(generic.ListView):
    template_name = 'tazakoom/rukovodstvo.html'

def emailUs(request):
    form = forms.Email()
    if request=='POST':
        form = forms.Email(request.POST)
        if form.is_valid():
            print('someone mailed you')
    return render(request,'tazakoom/emailUS.html',{'form':form})