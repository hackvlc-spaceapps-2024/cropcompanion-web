import sys
class SituationFactory:
    def solar(self):
        action = {
            'data': {
                'T2M': 27.51,
                'SI_EF_TILTED_HORIZONTAL': 	26.14,
                'GWETPROF': 0.31,
                'QV2M': 7.24,
                'PRECTOTCORR': 0
            },
            'action': {
                'ok': False,
                'description': 'High solar irradiance, cover and irrigate',
                'cover': True,
                'irrigate': True
            }
        }
        return action
    
    def cloudy(self):
        action = {
            'data': {
                'T2M': 21.34,
                'SI_EF_TILTED_HORIZONTAL': 	12.09,
                'GWETPROF': 0.51,
                'QV2M': 9.64,
                'PRECTOTCORR': 0
            },
            'action': {
                'ok': True,
                'description': 'Climate stable',
                'cover': False,
                'irrigate': False
            }
        }
        return action

    def rainy(self):
        action = {
            'data': {
                'T2M': 10.77,
                'SI_EF_TILTED_HORIZONTAL': 	0,
                'GWETPROF': 0.74,
                'QV2M': 13.64,
                'PRECTOTCORR': 4.22

            },
            'action': {
                'ok': False,
                'description': 'Critical weather, heavy rain',
                'cover': True,
                'irrigate': False
            }
        }
        print('BBBBBBBBBBBBBB', action, file=sys.stderr)
        return action