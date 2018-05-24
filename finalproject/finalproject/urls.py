"""
Definition of urls for finalproject.
"""

from datetime import datetime
from app.views import *
from app import views
from django.conf.urls import url
import django.contrib.auth.views
# import app.views as core_views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

from django.conf.urls import url
from app import views

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^tournaments/$', views.TournamentsView.as_view(), name='tournaments'),
    url(r'^fighters/$', app.views.fighters, name='fighters'),
    url(r'^newtournament/$', app.views.newTournament, name='newtournament'),
    url(r'^newfighter/$', app.views.newFighter, name='newfighter'),
    url(r'^signup/$', app.views.signup, name='signup'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
