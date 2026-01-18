from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Election, Candidate, Vote
from .forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Incorrect username/password')
    else:
        form = LoginForm()

    return render(request, 'login.html', { 'form': form })

@login_required(login_url='/login/')
def election_list(request):
    return render(request, 'election_list.html')

@login_required(login_url='/login/')
def signout(request):
    logout(request)

    return redirect('login')