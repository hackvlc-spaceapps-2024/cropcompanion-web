class Repository:
    status = [
        {
            'ok': True
        }
    ]

    @staticmethod
    def show():
        return Repository.status
