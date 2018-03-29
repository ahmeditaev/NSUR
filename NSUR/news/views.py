from django.views import generic
from . import models
from django.utils.timezone import now
from . import forms
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector
from Links.models import Facebook,VK,Tumblr,Twitter,Dribble,Pinterest





# Create your views here.
def mainPage(request):
    firstNews = models.News.objects.filter(published__lte=now()).order_by('-published')[:1]
    middleNews = models.News.objects.filter(published__lte=now()).order_by('-published')[1:4]
    downNews = models.News.objects.filter(published__lte=now()).order_by('-published')[4:7]
    lastNews = models.News.objects.filter(published__lte=now()).order_by('-published')[7:9]


    facebook,dribble,pinterest,tumblr,twitter,vk,press,photo,video = context()

    emailUsFooter(request)

    return render(request, 'home.html', {'middle':middleNews,'first':firstNews,'last':downNews,'down':lastNews,
                                         'press':press,
                                         'photo':photo,'video':video,'facebook':facebook,
                                        'dribble':dribble,'pinterest':pinterest,'tumblr':tumblr,
                                         'twitter':twitter,'vk':vk})

def postListView(request):
    facebook,dribble,pinterest,tumblr,twitter,vk,press,photo,video = context()
    posts = models.News.objects.all()
    pagin = paginate(request,posts)
    emailUsFooter(request)
    return render(request, 'posts/post_list.html', {'object_list':pagin, 'press':press,
                                         'photo':photo,'video':video,'facebook':facebook,
                                        'dribble':dribble,'pinterest':pinterest,'tumblr':tumblr,
                                         'twitter':twitter,'vk':vk})



def postDetailsView(request,pk):
    try:
        details = models.News.objects.get(pk=pk)
    except models.News.DoesNotExist:
        obj = models.News.objects.filter(published__lte=now()).latest('published')
        details = models.News.objects.get(pk=obj.pk)
    facebook,dribble,pinterest,tumblr,twitter,vk,press,photo,video = context()
    emailUsFooter(request)
    return render(request, 'posts/post_detail.html', {'details':details, 'press':press,
                                         'photo':photo,'video':video,'facebook':facebook,
                                        'dribble':dribble,'pinterest':pinterest,'tumblr':tumblr,
                                         'twitter':twitter,'vk':vk})






class AboutUs(generic.ListView):
    template_name = 'tazakoom/aboutus.html'
class Rukovodstvo(generic.ListView):
    template_name = 'tazakoom/rukovodstvo.html'

def emailUs(request):
    form = forms.Email()
    facebook,dribble,pinterest,tumblr,twitter,vk,press,photo,video = context()

    if request.method=='POST':
        form = forms.Email(request.POST)
        subject = request.POST.get('tel')
        message = request.POST.get('text')
        fromemail = request.POST.get('email')
        copy = request.POST.get('sendBack')
        if subject and message and fromemail:
            print('hey')
            if copy:
                send_mail(subject, message, fromemail, ['batyrbeknazik123@gmail.com',fromemail])
            else:
                send_mail(subject, message, fromemail, ['batyrbeknazik123@gmail.com'])
            print('someone mailed you')
    return render(request,'tazakoom/emailUS.html',{'form':form,'facebook':facebook,
                                        'dribble':dribble,'pinterest':pinterest,'tumblr':tumblr,
                                         'twitter':twitter,'vk':vk})

def emailUsFooter(request):
    formFooter = forms.EmailFooter()
    facebook,dribble,pinterest,tumblr,twitter,vk,press,photo,video = context()


    if request.method == 'POST':
        formFooter = forms.EmailFooter(request.POST or None)
        message = request.POST.get('textFooter')
        subject = request.POST.get('textFooter')
        fromemail = request.POST.get('emailFooter')

        if subject and message and fromemail:
            send_mail(subject, message, fromemail, ['batyrbeknazik123@gmail.com'])

    return render(request, 'footers/main.html', {'formFooter': formFooter,'facebook':facebook,
                                        'dribble':dribble,'pinterest':pinterest,'tumblr':tumblr,
                                         'twitter':twitter,'vk':vk})




def search(request):
    press = models.PressClipping.objects.filter(published__lte=now()).order_by('-published')[:6]
    photo = models.PhotoMediaBox.objects.filter(published__lte=now()).order_by('published')[:4]
    video = models.VideoMediaBox.objects.filter(published__lte=now()).order_by('-published')[:4]
    facebook = Facebook.objects.filter(published__lte=now()).order_by('-published')[:1]
    dribble = Dribble.objects.filter(published__lte=now()).order_by('-published')[:1]
    pinterest = Pinterest.objects.filter(published__lte=now()).order_by('-published')[:1]
    tumblr = Tumblr.objects.filter(published__lte=now()).order_by('-published')[:1]
    twitter = Twitter.objects.filter(published__lte=now()).order_by('-published')[:1]
    vk = VK.objects.filter(published__lte=now()).order_by('-published')[:1]


    print('search')
    query = request.GET.get("q")

    queryset_list = models.News.objects.filter(Q(title__icontains=query) |
                                               Q(text__icontains=query) |
                                               Q(quote__icontains=query) |
                                               Q(quoteAuthor__icontains=query)).distinct().order_by('-published')

    queryset_list = paginate(request,queryset_list)
    context = { 'object_list': queryset_list,
                   'posts': queryset_list,
                   'press': press, 'photo': photo,
                   'video': video,'facebook':facebook,
                                        'dribble':dribble,'pinterest':pinterest,'tumblr':tumblr,
                                         'twitter':twitter,'vk':vk

                }

    return render(request, 'posts/post_list.html', context)






def paginate(request,queryset_list):
    page = request.GET.get('page')
    paginator = Paginator(queryset_list, 8)
    print('search3')

    try:
        queryset = paginator.page(page)

    except PageNotAnInteger:
        print('hey1')
        queryset = paginator.page(1)
    except EmptyPage:
        print('hey2')
        queryset = paginator.page(paginator.num_pages)

    return queryset


def context():
    facebook = Facebook.objects.filter(published__lte=now()).order_by('-published')[:1]
    dribble = Dribble.objects.filter(published__lte=now()).order_by('-published')[:1]
    pinterest = Pinterest.objects.filter(published__lte=now()).order_by('-published')[:1]
    tumblr = Tumblr.objects.filter(published__lte=now()).order_by('-published')[:1]
    twitter = Twitter.objects.filter(published__lte=now()).order_by('-published')[:1]
    vk = VK.objects.filter(published__lte=now()).order_by('-published')[:1]

    press = models.PressClipping.objects.filter(published__lte=now()).order_by('-published')[:6]
    photo = models.PhotoMediaBox.objects.filter(published__lte=now()).order_by('-published')[:4]
    video = models.VideoMediaBox.objects.filter(published__lte=now()).order_by('-published')[:4]

    return facebook,dribble,pinterest,tumblr,twitter,vk,press,photo,video



