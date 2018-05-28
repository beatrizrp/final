"""
Definition of views.
"""

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth.models import User


from .forms import NewTournamentForm, NewFighterForm, SignUpForm
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

from .models import Fighter, Tournament, Combat

from django.utils import timezone

from django.core.urlresolvers import reverse



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

class TournamentsView(ListView):
    template_name = "app/tournaments.html"
    title = "Lista de Torneos"
    model = Tournament

    def tournaments(self):
        return Tournament.objects.all()

    def ctournament(request, t_id):
        winners = Tournament.celebrateTournament(t_id)
        return render(request, 'app/tournamentresult.html', {'data': winners})






class FightersView(ListView):
    template_name = "app/fighters.html"
    title = "Lista de Luchadores"
    model = Fighter

    def fighters(self):
        return Fighter.objects.all()





def fighters(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/fighters.html',
        {
            'title':'Fighters',
            'message':'Fighters page',
            'year':datetime.now().year,
        }
    )

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form': form})


def newTournament(request):
    if request.method == 'POST':
        form = NewTournamentForm(request.POST)
        if form.is_valid():
            ntorneo = form.save()
            return HttpResponseRedirect('/')
    else:
        form = NewTournamentForm()
    return render(request, 'app/newtournament.html', {'form':form})

def newFighter(request):
    if request.method == 'POST':
        form = NewFighterForm(request.POST)
        if form.is_valid():
            ntorneo = form.save()
            return HttpResponseRedirect('/')
    else:
        form = NewFighterForm()
    return render(request, 'app/newfighter.html', {'form':form})


