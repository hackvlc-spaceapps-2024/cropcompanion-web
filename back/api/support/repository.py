from api.support.situation_factory import SituationFactory

class Repository:
    status = []
    warning = False

    @staticmethod
    def show():
        return Repository.status
    
    @staticmethod
    def get_last():
        return Repository.status[-1]
    
    @staticmethod
    def save(status):
        if Repository.warning:
            Repository.warning()
        else:
            Repository.status.insert(0, status)

    def warning():
        Repository.warning = True

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
        Repository.status.insert(0, warning_status)

        return Repository.get_last()
    
    @staticmethod
    def purge():
        Repository.status = []
