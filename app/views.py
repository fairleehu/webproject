# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from app.forms import *
from django.views.decorators.csrf import csrf_exempt
from app.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


@csrf_exempt
def index(request):
    return render(request, 'app/index.html')


@csrf_exempt
def user_login(request):
    context_dict = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                q = User.objects.filter(username=username)
                q1 = AtUser.objects.filter(user=q)
                if q1.filter(userJob='员工'):
                    return HttpResponseRedirect('/app/userlog/')
                else:
                    return HttpResponseRedirect('/app/managlog/')
            else:
                context_dict['disabled_account'] = True
                return render_to_response('app/login.html', context_dict)
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            context_dict['bad_details'] = True
            return render_to_response('app/login.html', context_dict)
    else:
        return render_to_response('app/login.html', context_dict)


@csrf_exempt
def user_register(request):
    # Boolean telling us whether registration was successful or not.
    # Initially False; presume it was a failure until proven otherwise!
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response('app/register.html', {'user_form': user_form, 'profile_form': profile_form,
                                                    'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/app/')


@csrf_exempt
def userlog(request):
    return render_to_response('app/user.html')


@csrf_exempt
def managlog(request):
    return render_to_response('app/manag.html')


@csrf_exempt
def managsend(request):
    content_dict = {}
    if request.method == 'POST':
        stype = request.POST.get('typeid', '')
        scontent = request.POST.get('text', '')
        sdate = request.POST.get('date', '')
        if stype == "" and scontent == "":
            content_dict['ty'] = True
            return render_to_response('app/managsend.html', content_dict)
        else:
            temp = AtSend(sendType=stype, sendText=scontent, sendTime=sdate)
            temp.save()
            content_dict['ty'] = False
            return render_to_response('app/managsend.html', content_dict)
    return render_to_response('app/managsend.html', content_dict)
