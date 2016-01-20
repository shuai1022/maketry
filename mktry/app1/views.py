from django.shortcuts import render
from django.http import HttpResponse
from .models import try_carousel
from django.template import RequestContext,loader

def add(request):
    template = loader.get_template('app1/add.html')
    return HttpResponse(template.render())

def add1(request):

    tc = try_carousel(request);
    tc.save();
    return HttpResponse('ok')

def delete(request):
    return HttpResponse('delete')

def update(request):
    return HttpResponse('update')

def list(request):
    content_list = try_carousel.objects.all()
    template = loader.get_template('app1/list.html')
    context = RequestContext(request,{'content_list':content_list})
    return HttpResponse(template.render(context))