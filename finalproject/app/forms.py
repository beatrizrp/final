"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
from .models import Tournament, Fighter

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class NewTournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'create_date', 'start_date', 'numberPlayers', 'type', 'strengthWeigth', 'dexterityWeigth', 'resistanceWeigth']

class NewFighterForm(forms.ModelForm):
    class Meta:
        model = Fighter
        fields = ['userId', 'alias', 'strength', 'dexterity', 'resistance']



