from django.shortcuts import render #type: ignore
from django.http import JsonResponse # type: ignore
from rest_framework.decorators import api_view # type: ignore
from django.core import serializers

from api.support.requester import Requester
from api.support.situation_factory import SituationFactory
from api import models

import json, sys

requester = Requester()
factory = SituationFactory()
# Create your views here.
@api_view(['GET'])
def monthly(request):
    return requester.get_monthly()

@api_view(['GET'])
def clima(request):
    return requester.get_clima()

@api_view()
def solar(request):
    action = factory.solar()

    return JsonResponse(action)

@api_view()
def cloudy(request):
    action = factory.cloudy()

    return JsonResponse(action)

@api_view()
def rainy(request):
    action = factory.rainy()

    # serialized_action = json.dumps(action)
    # print('AAAAAAAAAAAAAAAAA', serialized_action, file=sys.stderr)
    return JsonResponse(action)

@api_view(['GET'])
def orders(request):
    try:
        orders = models.Orders.objects.all().order_by('-id').first()
    except:
        orders = {}

    orders = orders.serialise()
    return JsonResponse(orders)


@api_view(['POST'])
def status(request):
    print('POST Status', file=sys.stderr)
    __body = {
        'T2M': 27.51, #TEMP
        'SI_EF_TILTED_HORIZONTAL': 	26.14, #SOLAR LIGHT
        'GWETPROF': 0.31, #HUMMIDITY IN SOILD
        'QV2M': 7.24, #HUMMIDIFY SPECIFIC
        'PRECTOTCORR': 0 #WATER HEIGHT
        }
    return JsonResponse({'message': 'POST'})

@api_view(['GET'])
def status(request):

    print('GET Status')
    return JsonResponse({'message': 'GET'})
