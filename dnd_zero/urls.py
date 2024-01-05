from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('handbook', views.handbook, name='handbook'),
    path('about', views.about, name='about'),
    path('legends', views.legends, name='legends'),

    path('create_character/', views.create_character, name='create_character'),
    path('character/<uuid:pk>/', views.CharacterDetailView.as_view(), name='character_detail'),
    path('my_characters/', views.MyCharactersList.as_view(), name='my_characters'),
    path('characters_list/', views.AllCharactersList.as_view(), name='all_characters'),


    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),

    path('master/<slug:username>/', views.MasterDetailView.as_view(), name='master_detail'),

]
