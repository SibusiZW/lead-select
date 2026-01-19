from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.election_list, name='home'),
    path('<int:pk>/', views.election_detail, name='election'),
    path('vote/<int:pk>', views.vote, name='vote'),
    path('stats/', views.stats_view, name='stats'),
    path('logout/', views.signout, name='signout'),
]