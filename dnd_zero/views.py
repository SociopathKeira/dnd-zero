from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import generic
from .models import Character, User
from .forms import SignUpForm, SignInForm, CharacterForm

# Create your views here.


def index(request):
    return render(request, 'dnd_zero/index.html')


def handbook(request):
    return render(request, 'dnd_zero/handbook.html')


def about(request):
    return render(request, 'dnd_zero/about.html')


def legends(request):
    return render(request, 'dnd_zero/legends,html')


def create_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST, user=request.user)
        if form.is_valid():
            character = form.save()
            return redirect('character/', pk=character.pk)
    else:
        form = CharacterForm(user=request.user)
    return render(request, 'create_character.html', {'form': form})


class CharacterDetailView(LoginRequiredMixin, generic.DetailView):
    model = Character
    context_object_name = 'character'
    template_name = 'character_detail.html'


class MyCharactersList(LoginRequiredMixin, generic.ListView):
    model = Character
    context_object_name = 'character_list'
    template_name = 'my_characters_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Character.objects.filter(master=self.request.user.id)


class AllCharactersList(LoginRequiredMixin, generic.ListView):
    model = Character
    context_object_name = 'character_list'
    template_name = 'all_characters_list.html'
    paginate_by = 15

    def get_queryset(self):
        return Character.objects.order_by('-master')


class MasterDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'master_detail.html'



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid form data.')
    else:
        form = SignInForm()
    return render(request, 'registration/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('home')
