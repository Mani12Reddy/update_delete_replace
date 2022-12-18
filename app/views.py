from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q

def display_topic(request):

    LTO=Topic.objects.all()
    d={'LTO':LTO}

    return render(request,'display_topic.html',d)


def display_webpages(request):
    LWO=Webpages.objects.all()
    LWO=Webpages.objects.filter(topic_name='Cricket')
    LWO=Webpages.objects.exclude(topic_name='Cricket')
    LWO=Webpages.objects.all()[2:5:]
    LWO=Webpages.objects.all()
    LWO=Webpages.objects.all().order_by('name')
    LWO=Webpages.objects.filter(topic_name='Cricket').order_by('-name')

    # LWO=Webpages.objects.all().order_by(Length('name'))
   # LWO=Webpages.objects.all().order_by(Length('name').desc())

    LWO=Webpages.objects.filter(name__startswith='m')
    LWO=Webpages.objects.filter(name__endswith='i')
    LWO=Webpages.objects.filter(name__contains='m')
    LWO=Webpages.objects.filter(name__in=('Mani','Kohli'))
    LWO=Webpages.objects.filter(name__regex='^M\W{6}')
    LWO=Webpages.objects.all()
    LWO=Webpages.objects.filter(Q(topic_name='Cricket') & Q(name__startswith='K'))
    LWO=Webpages.objects.all()
    LWO=Webpages.objects.filter(Q(topic_name='Foot Ball') | Q(url__endswith='in'))

    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)

def access(request):
    LAO=Accessrecords.objects.all()
    LAO= Accessrecords.objects.all()
    LAO=Accessrecords.objects.filter(date='1999-11-01')    
    LAO=Accessrecords.objects.filter(date__year='2022')
    LAO=Accessrecords.objects.filter(date__month='1')    
    LAO=Accessrecords.objects.filter(date__day='14')    
    LAO=Accessrecords.objects.filter(date__gte='1999-11-01')
    LAO=Accessrecords.objects.filter(date__lte='1999-11-01')
    LAO=Accessrecords.objects.filter(date__year__gte='1999')

    d={'LAO':LAO}
    return render(request,'access.html',d)



def update_webpages(request):
    #Webpage.objects.filter(topic_name='Boxing').update(name='Naresh',url='https://Naresh.in')
    #Webpage.objects.filter(name='ABCDE').update(topic_name='Foot Ball')
    T=Topic.objects.get_or_create(topic_name='Cricket')[0]
    T.save()
    Webpages.objects.update_or_create(name='ABD',defaults={'topic_name':T,'url':'https://ABD.in'})
    LWO=Webpages.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)


def delete_webpages(request):
    #Webpage.objects.filter(topic_name='Cricket').delete()
    
    Webpages.objects.all().delete()
    LWO=Webpages.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)








