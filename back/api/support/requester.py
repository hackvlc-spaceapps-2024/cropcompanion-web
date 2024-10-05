from django.http import JsonResponse # type: ignore

import requests

CLIMATOLOGY_URL = 'https://power.larc.nasa.gov/api/temporal/climatology/point?start=2020&end=2022&latitude=39.39327127119697&longitude=-0.3626686950900597&community=ag&parameters=PRECTOTCORR%2CPRECTOTCORR_SUM%2CSI_EF_MIN_TILTED_SURFACE%2CSI_EF_MAX_TILTED_SURFACE%2CSI_EF_TILTED_SURFACE&format=json&header=true'
MONTHLY_URL = 'https://power.larc.nasa.gov/api/temporal/monthly/point?start=2020&end=2022&latitude=39.40097177494886&longitude=-0.3608408203687458&community=ag&parameters=GWETPROF%2CT2M%2CQV2M%2CPRECTOTCORR%2CPRECTOTCORR_SUM&format=json&header=true'

class Requester():
    def __init__(self) -> None:
        # url = 
        LATITUDE = 39.40097177494886
        LONGITUDE = -0.3608408203687458

        parameters = [
            'PRECTOTCORR', #PRECIPITATION CORRECTED
            'PRECTOTCORR_SUM', #PRECIPITATION CORRECTED SUM
            'SI_EF_MIN_TILTED_SURFACE', #MIN SOLAR IRRADIANCE
            'SI_EF_MAX_TILTED_SURFACE', #MAX SOLAR IRRADIANCE
            'SI_EF_TILTED_SURFACE' #SOLAR IRRADIANCE
        ]

        montly_params = [
            'GWETPROF', #PROFILE SOIL MOISTURE
            'T2M', #TEMPERATURE AT 2m RANGE
            'QV2M', #SPECIFIC HUMMICITY AT 2m RANGE
            'PRECTOTCORR', #PRECIPITATION CORRECTED
            'PRECTOTCORR_SUM', #PRECIPITATION CORRECTED SUM
        ]
    
    def get_monthly(self):
        r = requests.get(MONTHLY_URL)

        return JsonResponse(r.json())
    
    def get_clima(self):
        r = requests.get(CLIMATOLOGY_URL)

        return JsonResponse(r.json())
    

