from django.urls import path #type: ignore

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('monthly', views.monthly, name='monthly'),
    path('clima', views.clima, name='clima'),
    path('demo/solar', views.solar, name='solar'),
    path('demo/cloudy', views.cloudy, name='cloudy'),
    path('demo/rainy', views.rainy, name='rainy'),
    path('orders', views.orders, name='orders')
]
