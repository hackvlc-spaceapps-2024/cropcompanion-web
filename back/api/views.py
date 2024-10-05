from django.shortcuts import render #type: ignore
from rest_framework.decorators import api_view # type: ignore

from api.support.requester import Requester

requester = Requester()
# Create your views here.
@api_view(['GET'])
def monthly(request):
    return requester.get_monthly()

@api_view(['GET'])
def clima(request):
    return requester.get_clima()