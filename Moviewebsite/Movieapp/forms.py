
from django.forms import ModelForm
from .models import User_registration, Add_movies
from django import forms


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User_registration
        fields = ['firstname','lastname','username','email','password']


class MovieForm(forms.ModelForm):
    class Meta:
        model=Add_movies
        fields=['movie_title','poster','description','release_date','actors','category','YouTube_trailer_link']