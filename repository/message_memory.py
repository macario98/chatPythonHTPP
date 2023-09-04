from domain.message import Domain
from typing import Dict, Tuple
class Repository:
    dataMemory: Dict[int, Domain]
    lastId:int

    def __init__(self) -> None:
        self.dataMemory = {}
        self.lastId = 0

    def Get(self, id:int)->Domain:
        message = self.dataMemory.get(id, 0)
        return message
    
    def GetAll(self):
        return self.dataMemory
    
    def Save(self, message:Domain)-> Tuple[int, Exception]:
        self.dataMemory[self.lastId] = message
        self.lastId+=self.lastId

        return (self.lastId, None)