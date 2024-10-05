from django.urls import path #type: ignore

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('monthly', views.monthly, name='monthly'),
    path('clima', views.clima, name='clima'),
    # path('users/', views.users, name='users'),
    # path('login/', views.login, name='login'),
    # path('inventory/', views.inventory, name='inventory'),
    # path('rest-auth/google/', views.google_login, name='google_login')
]