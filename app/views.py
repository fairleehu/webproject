from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from app.forms import *
from django.views.decorators.csrf import csrf_exempt
from app.models import *
# Create your views here.

@csrf_exempt
def index(request):
    return render(request, 'app/index.html')

@csrf_exempt
def user_login(request):
    return render(request, 'app/login.html')

@csrf_exempt
def user_register(request):
    deptn = Dept.objects.all()
    # Boolean telling us whether registration was successful or not.
    # Initially False; presume it was a failure until proven otherwise!
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            un = request.POST['qname']
            em = request.POST['qemail']
            ps = request.POST['qpasswd']
            job = request.POST['qjob']
            dept = request.POST['qdept']
            AtUser.objects.create(username=un, email=em,
                                  password=ps, userDept=dept, userJob=job)

        # if user_form.is_valid() and profile_form.is_valid():
        #user = user_form.save()
        # user.set_password(user.password)
        # user.save()

        #profile = profile_form.save(commit=False)
        #profile.user = user

        # if 'picture' in request.FILES:
        #profile.picture = request.FILES['picture']
        # profile.save()
        #registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    # Render and return!
    return render_to_response(
        'app/register.html', {'user_form': user_form, 'profile_form': profile_form,
                              'registered': registered,
                              'deptn': deptn})
