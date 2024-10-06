class Repository:
    status = []

    @staticmethod
    def show():
        return Repository.status
    
    @staticmethod
    def get_last():
        return Repository.status[0]
    
    @staticmethod
    def save(status):
        Repository.status.insert(0, status)
    
    @staticmethod
    def purge():
        Repository.status = []
