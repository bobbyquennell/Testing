from django.shortcuts import render,HttpResponse,redirect,render_to_response,HttpResponseRedirect
from django.forms.utils import ErrorDict
from . import forms

def index(request):
    l1 = forms.Login()
    ret ={'data':None,'error':''}
    ret['data'] = l1
    if request.method == 'POST':
        form = forms.Login(request.POST)
        #request.POST is a dictionary which includes all data submitted by user
        print type(form),form
        if form.is_valid():    # To verify user's input
            pass
        else:
            er = form.errors.as_data().values()[0][0].messages[0]
            print type(er)
            ret['error'] = er
            ret['data'] = form
        return render_to_response('app01/index.html',ret)
    return render_to_response('app01/index.html',ret)


# def contact(request):
#     if request.method == 'POST':
#         form = forms.ContactForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             send_mail(
#                 cd['subject'],
#                 cd['message'],
#                 cd.get('email', 'noreply@example.com'),
#                 ['siteowner@example.com'],
#             )
#             return HttpResponseRedirect('/contact/thanks/')
#     else:
#         form = forms.ContactForm(
#             initial={'subject': 'I love your site!'}
#         )
#     return render(request, 'app01/index.html', {'form': form})












