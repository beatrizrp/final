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
from .countries import COUNTRIES

countries = COUNTRIES

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

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='*')
    last_name = forms.CharField(max_length=30, required=True, help_text='*')
    email = forms.EmailField(max_length=254, help_text='*')    
    country = forms.ChoiceField(required=True, help_text='*', choices = countries)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class NewTournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'create_date', 'start_date', 'numberRounds', 'strengthWeigth', 'dexterityWeigth', 'resistanceWeigth', 'fighters']

class NewFighterForm(forms.ModelForm):
    class Meta:
        model = Fighter
        fields = ['userId', 'alias', 'strength', 'dexterity', 'resistance']

