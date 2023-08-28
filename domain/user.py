import datetime
class Domain:
    id:int
    name:str
    lastSeen:datetime
    def __init__(self, name = "", lastSeen = datetime.datetime.utcnow()) -> None:
        self.id = 0
        self.name = name
        self.lastSeen = lastSeen