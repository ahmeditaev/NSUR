from django.shortcuts import render
from django.views import generic
from . import models
from django.utils.timezone import now
from . import forms
from .forms import Email
from django.core.mail import send_mail,EmailMessage,BadHeaderError
from django.http import HttpResponse


# Create your views here.
def mainPage(request):
    firstNews = models.News.objects.filter(published__lte=now()).order_by('-published')[:1]
    middleNews = models.News.objects.filter(published__lte=now()).order_by('-published')[1:4]
    downNews = models.News.objects.filter(published__lte=now()).order_by('-published')[4:7]
    lastNews = models.News.objects.filter(published__lte=now()).order_by('-published')[7:9]
    press = models.PressClipping.objects.filter(published__lte=now()).order_by('-published')[:6]
    photo = models.PhotoMediaBox.objects.filter(published__lte=now()).order_by('-published')[:4]
    video = models.VideoMediaBox.objects.filter(published__lte=now()).order_by()[:4]
    return render(request, 'home.html', {'middle':middleNews,'first':firstNews,'last':downNews,'down':lastNews, 'press':press,
                                         'photo':photo,'video':video})

class PostListView(generic.ListView):
    model = models.News
    template_name = 'posts/post_list.html'

class PostDetailView(generic.DetailView):
    model = models.News
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['details'] = models.News.objects.get(pk=self.object.pk)
        context['press'] = models.PressClipping.objects.filter(published__lte=now()).order_by('-published')[:6]
        return context

def postDetailsView(request):
    details = models.News
    press = models.PressClipping.objects.filter(published__lte=now()).order_by('-published')[:6]
    return render(request, 'posts/post_detail.html', {'details':details, 'press':press})






class AboutUs(generic.ListView):
    template_name = 'tazakoom/aboutus.html'
class Rukovodstvo(generic.ListView):
    template_name = 'tazakoom/rukovodstvo.html'

def emailUs(request):
    form = forms.Email()
    if request.method=='POST':
        form = forms.Email(request.POST)
        subject = request.POST.get('tel')
        message = request.POST.get('text')
        fromemail = request.POST.get('email')
        if subject and message and fromemail:
            print('hey')
            send_mail(subject, message, fromemail, ['batyrbeknazik123@gmail.com'])
            print('someone mailed you')
    return render(request,'tazakoom/emailUS.html',{'form':form})


def send_email(subject,message,fromemail,toemail):
    email = EmailMessage(subject,message,fromemail,toemail)
    email.send()












