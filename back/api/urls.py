from django.urls import path #type: ignore

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('monthly', views.monthly, name='monthly'),
    path('clima', views.clima, name='clima'),
    path('status', views.status, name='status'),
    path('get_status', views.get_status, name='get_status'),
    path('warning', views.warning, name='warning'),
    path('purge', views.purge, name='purge'),
    path('demo/solar', views.solar, name='solar'),
    path('demo/cloudy', views.cloudy, name='cloudy'),
    path('demo/rainy', views.rainy, name='rainy'),
    path('orders', views.orders, name='orders'),
    path('set_orders', views.set_orders, name='set_orders')
]
