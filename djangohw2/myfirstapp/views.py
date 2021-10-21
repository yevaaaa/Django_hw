from django.shortcuts import render
from django.http import HttpResponse


from myfirstapp.models import Human


def about(request):
    v = Human.objects.get(id=2)
    return render(request, 'myfirstapp/about.html', {'context': v})


def human(request):
    h = Human.objects.get(id=1)
    return render(request, 'myfirstapp/human.html', {'context': h})