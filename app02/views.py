from django.shortcuts import render,HttpResponse

# Create your views here.


def ajax(request):
    print request.POST
    return HttpResponse('OK')