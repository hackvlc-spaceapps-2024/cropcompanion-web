from django.shortcuts import render #type: ignore
from django.http import JsonResponse # type: ignore
from rest_framework.decorators import api_view # type: ignore
from django.core import serializers

from api.support.requester import Requester
from api.support.repository import Repository
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
        orders = models.Orders.objects.all().values_list('id', flat=True).order_by('-id').first()
    except:
        orders = []

    orders = serializers.serialize("json", orders)
    return JsonResponse(orders)


@api_view(['POST'])
def status(request):
    print('POST Status', file=sys.stderr)
    body_unicode = request.body.decode('utf-8')
    print('BODY', body_unicode, file=sys.stderr)

    serialized = json.loads(body_unicode)
    # transformed = 

    Repository.save(serialized)
    
    return JsonResponse(Repository.show(), safe=False)

@api_view(['GET'])
def purge(request):
    Repository.purge()

    return JsonResponse({ 'message': 'Database purged' })

@api_view(['GET'])
def get_status(request):

    print('GET Status')
    return JsonResponse({ 'message': 'GET' })
