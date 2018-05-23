"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from .forms import NewTournamentForm, NewFighterForm

from .models import Fighter, Tournament, Combat

from django.utils import timezone


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

def tournaments(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tournaments.html',
        {
            'title':'Tournaments',
            'message':'Tournaments page',
            'year':datetime.now().year,
        }
    )

def signup(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/signup.html',
        {
            'title':'Tournaments',
            'message':'Tournaments page',
            'year':datetime.now().year,
        }
    )



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
   


