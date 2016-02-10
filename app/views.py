from django.shortcuts import render,HttpResponse,render_to_response,HttpResponseRedirect,redirect
from . import models

#django.db.models.manager.Manager


# def artical(requeset,year,month,artical_id):
#     return HttpResponse('DDDD')


def add(request,name):
    models.Role.objects.create(role_name = name)
    return HttpResponse("add")


def delete(request,id):
    # models.Role.objects.get(id = id).delete(), which will pop up error message when id doesn't exist
    models.Role.objects.filter(id = id).delete()
    return HttpResponse("delete")


def update(request,id,name):
    # models.Role.objects.filter(id = id).update(role_name = name)
    obj = models.Role.objects.get(id = id)
    obj.role_name = name
    obj.save()
    return HttpResponse("update")

def view(request,name):
    list = models.Role.objects.filter(role_name__contains = name)
    for item in list:
        print item.id

    return HttpResponse("view")


# workaround to register a user into database
# def register(request):
#     r1 = models.Role.objects.create(role_name='admin')
#     r2 = models.Role.objects.create(role_name='user')
#     u1 = models.UserInfo.objects.create(name="Yang",password="123",
#                                         email='yang.wang04@gmail.com',gender='f',role_id=r1)
#     g1 = models.Group.objects.create(group_name='groupA')
#     g2 = models.Group.objects.create(group_name='groupB')
#     g1.user.add(u1)
#     g2.user.add(u1)
#     return HttpResponse("Register is successfully!")


def login(request):
    ret = {'status': ''}
    if request.method == 'POST':
        user = request.POST.get('username',None) #To provide a default value when we cannot find 'username' and 'password'
        pwd = request.POST.get('password',None)
        is_empty = all([user,pwd])
        if is_empty:
            count = models.UserInfo.objects.filter(name = user, password = pwd).count()
            if count == 1:
                return redirect('app/index/')
            else:
                ret['status'] = 'Username or password is invalid, please try again.'
                return render_to_response('login.html',ret)
        else:
            ret['status'] = 'Username or password cannot not empty.'
            return render_to_response('login.html',ret)
    else:
        return render_to_response('login.html',ret)

def index(request):
    return render_to_response('index.html')


def host(request):
    ret = {'status':'','group':None,'data':None}
    group_name = models.Group.objects.all()
    ret['group'] = group_name
    return render_to_response('host.html',ret)

