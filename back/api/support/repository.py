from api.support.situation_factory import SituationFactory

import sys

class Repository:
    status = []
    alert = False

    @staticmethod
    def show():
        return Repository.status
    
    @staticmethod
    def get_last():
        return Repository.status[0]
    
    @staticmethod
    def save(status):
        print(Repository.alert, file=sys.stderr)
        if Repository.alert:
            Repository.warning()
            return
        else:
            Repository.status.insert(0, status)
        
        return

    def warning():
        if Repository.alert:
            Repository.alert = False
            return Repository.get_last()
        
        Repository.alert = True

        warning_status = {
                'Type': 0,
                'Prevition': {
                    'T2M': 35.89,
                    'SI_EF_TILTED_HORIZONTAL': 	26.14,
                    'GWETPROF': 0.31,
                    'QV2M': 7.24,
                    'PRECTOTCORR': 0
                },
                'action': {
                    'ok': False,
                    'description': 'High solar irradiance, cover and irrigate',
                    'cover': True,
                    'irrigate': True,
                    'light': False,
                }
            }
        Repository.status = [warning_status]

        return Repository.status
    
    @staticmethod
    def purge():
        Repository.status = []
