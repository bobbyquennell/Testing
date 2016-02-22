from django.shortcuts import render,HttpResponse,render_to_response,redirect
from . import models

# django.db.models.manager.Manager


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
#                                         email='yang.wang04@gmail.com',gender='f',role = r1)
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
                return redirect('/app/index/')
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


    asset_data = models.Asset.objects.all()
    ret['data'] = asset_data

    # asset_data = models.Asset.objects.filter(group__id=2)
    # print type(asset_data),asset_data
    # asset_data's type is also <class 'django.db.models.query.QuerySet'> and content is [<Asset: Asset object>, <Asset: Asset object>, <Asset: Asset object>]
    # Therefore, filter is the same as all function
    # ret['data'] = asset_data

# group's type is <class 'django.db.models.query.QuerySet'> and content is [<Group: Group object>, <Group: Group object>]
#And <Group: Group object> is an object which encapsulates class's attributes and a single record.
    group_data = models.Group.objects.all()

    # group is actually a list, which passed to ret['group'] as value
    ret['group'] = group_data


    # To add host information into database
    if request.method == 'POST':
        host_name = request.POST.get('hostname',None)
        ip_address = request.POST.get('ip',None)
        group_id = request.POST.get('group',None)
        group = models.Group.objects.get(id = group_id)
        is_empty = all([host_name,ip_address])
        if is_empty:
            print group,type(group),group_id,type(group_id)
            models.Asset.objects.create(host_name = host_name, group = group ,ip_address = ip_address)

        else:
            ret['status'] = 'Host name or IP is empty, please try again.'
            return render_to_response('host.html',ret)

# only filter group_name = 'groupB'
#         asset_data = models.Asset.objects.filter(group__group_name='groupB')
#         ret['data'] = asset_data
#
#         asset_data = models.Asset.objects.filter(group__id = 1)
#         ret['data'] = asset_data

    # print models.Asset.objects.filter(group__group_name='groupB').query

    return render_to_response('host.html',ret)


def add_many(request):

    u1 = models.UserInfo.objects.get(id = 2)
    g1 = models.Group.objects.get(id = 3)

    # method 1
    g1.user.add(u1)
    # print g1.user.add
    # <bound method ManyRelatedManager.add of <django.db.models.fields.related_descriptors.ManyRelatedManager object at 0x103e3a650>>

    # method 2
    u1.group_set.add(g1)

    return HttpResponse('Add successfully')


def asset(request):
    return render(request,'asset.html')




def audit(request):
    return render(request,'audit.html')





