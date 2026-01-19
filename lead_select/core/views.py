from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.db.models import Count
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
    elections = Election.objects.order_by('-date_created')

    return render(request, 'election_list.html', {'user': request.user, 'elections': elections})

@login_required(login_url='/login/')
def election_detail(request, pk):
    election = get_object_or_404(Election, pk=pk)
    candidates = Candidate.objects.filter(election=election)

    return render(request, 'election_detail.html', { 'election': election, 'candidates': candidates })

@login_required(login_url='/login/')
def signout(request):
    logout(request)

    return redirect('login')

@login_required(login_url='/login/')
def vote(request, pk):
    candidate = Candidate.objects.get(id=pk)

    obj = Vote(user=request.user, candidate=candidate, election=candidate.election)
    obj.save()
    return redirect('home')

def stats_view(request):
    elections = Election.objects.order_by('-date_created').annotate(total_votes=Count('votes'))

    return render(request, 'stats.html', { 'elections': elections })