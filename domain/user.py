import datetime
class Domain:
    id:int
    name:str
    lastSeen:datetime
    def __init__(self) -> None:
        self.id = 0
        self.name = ""
        self.lastSeen = datetime.datetime.now()