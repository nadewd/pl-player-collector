from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('players/', views.players_index, name='index'),
    path('players/<int:player_id>/', views.players_detail, name='detail'),
    path('players/create/', views.PlayerCreate.as_view(), name='players_create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='players_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='players_delete'),
    path('players/<int:player_id>/add_matchstats/', views.add_matchstats, name='add_matchstats'),
    path('players/<int:player_id>/assoc_teammate/<int:teammate_id>/', views.assoc_teammate, name='assoc_teammate'),
    path('players/<int:player_id>/unassoc_teammate/<int:teammate_id>/', views.unassoc_teammate, name='unassoc_teammate'),
    path('teammates/', views.TeammateList.as_view(), name='teammates_index'),
    path('teammates/<int:pk>/', views.TeammateDetail.as_view(), name='teammates_detail'),
    path('teammates/create/', views.TeammateCreate.as_view(), name='teammates_create'),
    path('teammates/<int:pk>/delete/', views.TeammateDelete.as_view(), name='teammates_delete'),
]

