from django import forms
from .models import Character
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'race', 'character_class', 'master', 'story1', 'story2', 'story3']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.fields['master'].initial = user if user else None
        self.fields['master'].widget = forms.HiddenInput()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Email is required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class SignInForm(AuthenticationForm):

    error_messages = {
        'invalid_login': ("Please enter a correct %(username)s and password. "
                          "Note that both fields may be case-sensitive."),
    }