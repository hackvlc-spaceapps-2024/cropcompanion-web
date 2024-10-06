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
        orders = models.Orders.objects.all().order_by('-id').first()
    except:
        orders = {}

    orders = orders.serialise() if orders else {}
    return JsonResponse(orders)


@api_view(['POST'])
def status(request):
    print('POST Status', file=sys.stderr)
    body_unicode = request.body.decode('utf-8')

    formated_body = json.loads(body_unicode)
    pretty_body = json.dumps(formated_body, indent=2)
    print(pretty_body, file=sys.stderr)

    if not Repository.warning:
        Repository.save(formated_body)
    
    return JsonResponse(Repository.get_last(), safe=False)

@api_view(['GET'])
def get_status(request):

    return JsonResponse(Repository.get_last(), safe=False)

@api_view(['GET'])
def warning(request):

    return JsonResponse(Repository.warning())

@api_view(['GET'])
def purge(request):
    Repository.purge()

    return JsonResponse({ 'message': 'Database purged' })

@api_view(['GET'])
def get_status(request):

    print('GET Status')
    return JsonResponse({ 'message': 'GET' })
