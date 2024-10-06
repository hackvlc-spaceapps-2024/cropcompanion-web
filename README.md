# PlantAssistant-web
TBD

# START

## Build container
- $ make build

Once build you can start or stop the containers without building again

## Start/stop the container
Start the container
- $ make up

Stop the container
- $ make down

## Get requests

### Monthly data
- Visit http://localhost:8000/v1/monthly

### Climatology data
- Visit http://localhost:8000/v1/clima

# DEMO

## First scenario (Solar Weather)
- http://localhost:8000/v1/demo/solar

## Second scenario (Cloudy Weather)
- http://localhost:8000/v1/demo/cloudy

## Third scenario (Rainy Weather)
- http://localhost:8000/v1/demo/rainy

### Info

All the scenarios are in the file back.api.support.situation_factory

#### Sample request

- T2M (Temperature)
- SI_EF_TILTED_HORIZONTAL (Solar Irradiance)
- GWETPROF (Soil Moisture)
- QV2M (Hummidity)
- PRECTOTCORR (Water Height)

``` JSON
{
    "data": {
        "T2M": 27.51, 
        "SI_EF_TILTED_HORIZONTAL": 26.14, 
        "GWETPROF": 0.31, 
        "QV2M": 7.24, 
        "PRECTOTCORR": 0
        }, 
        "action": {
            "ok": false, 
            "description": "High solar irradiance, cover and irrigate", 
            "cover": true, 
            "irrigate": true, 
            "light": false
        }
    }

```
# ENDPOINTS

## Update Station Status
POST - http://localhost:8000/v1/status

Update the station last data to the backend

GET - http://localhost:8000/v1/status

Get the station's last data
