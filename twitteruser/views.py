from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from twitteruser.models import TwitterUser
from twitteruser.forms import log_in, create_user

def index(request, id):
    if settings.AUTH_USER_MODEL:
        umodel = settings.AUTH_USER_MODEL
    else:
        return HttpResponseRedirect(reverse('log_in'))
    # add tweets by who user follows
    return render(request, 'index.html', {'umodel': umodel})

def UserPage(request, id):
    profile = TwitterUser.objects.get(id=id)
    return render(
        request,
        'profile.html',
        {'profile': profile}
    )

def UserLogin(request):
    if request.method == "POST":
        form = log_in(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            suser = authenticate(
                username=data['username'],
                password=data['password']
                )
            if suser:
                login(request, suser)
                return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('home'))
    form = log_in() #create log in form
    return render(
        request,
        'form.html',
        {'form': form}
    )

def create_user_view(request):
    if request.method == 'POST':
        form = create_user(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            x = TwitterUser.objects.create(
                name=data['name'],
                password=data['password']
            )
            if x:
                login(request, x)
                return HttpResponseRedirect(reverse('home'))
    form = create_user()
    return render(
        request,
        'form.html',
        {'form': form}
    )

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('log_in'))
