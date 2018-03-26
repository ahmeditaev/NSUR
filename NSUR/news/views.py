from django.views import generic
from . import models
from django.utils.timezone import now
from . import forms
from django.core.mail import send_mail
from django.shortcuts import render,get_object_or_404





# Create your views here.
def mainPage(request):
    firstNews = models.News.objects.filter(published__lte=now()).order_by('-published')[:1]
    middleNews = models.News.objects.filter(published__lte=now()).order_by('-published')[1:4]
    downNews = models.News.objects.filter(published__lte=now()).order_by('-published')[4:7]
    lastNews = models.News.objects.filter(published__lte=now()).order_by('-published')[7:9]
    press = models.PressClipping.objects.filter(published__lte=now()).order_by('-published')[:6]
    photo = models.PhotoMediaBox.objects.filter(published__lte=now()).order_by('-published')[:4]
    video = models.VideoMediaBox.objects.filter(published__lte=now()).order_by()[:4]

    emailUsFooter(request)

    return render(request, 'home.html', {'middle':middleNews,'first':firstNews,'last':downNews,'down':lastNews, 'press':press,
                                         'photo':photo,'video':video})

class PostListView(generic.ListView):
    model = models.News
    template_name = 'posts/post_list.html'


def postDetailsView(request,pk):
    try:
        details = models.News.objects.get(pk=pk)
    except models.News.DoesNotExist:
        obj = models.News.objects.filter(published__lte=now()).order_by('-id')[0]
        details = models.News.objects.get(pk=obj.pk)
    press = models.PressClipping.objects.filter(published__lte=now()).order_by('-published')[:6]
    photo = models.PhotoMediaBox.objects.filter(published__lte=now()).order_by('-published')[:4]
    video = models.VideoMediaBox.objects.filter(published__lte=now()).order_by()[:4]
    emailUsFooter(request)
    return render(request, 'posts/post_detail.html', {'details':details, 'press':press, 'photo':photo,'video':video})






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

def emailUsFooter(request):
    formFooter = forms.EmailFooter()
    if request.method == 'POST':
        formFooter = forms.EmailFooter(request.POST or None)
        message = request.POST.get('textFooter')
        subject = request.POST.get('textFooter')
        fromemail = request.POST.get('emailFooter')
        if subject and message and fromemail:
            send_mail(subject, message, fromemail, ['batyrbeknazik123@gmail.com'])
    return render(request, 'footers/main.html', {'formFooter': formFooter})

















