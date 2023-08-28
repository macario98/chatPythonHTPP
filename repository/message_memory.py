from ..domain import message
from typing import Dict, Tuple
class Repository:
    dataMemory: Dict[int, message.Domain]
    lastId:int

    def __init__(self) -> None:
        self.dataMemory = {}
        self.lastId = 0

    def Get(self, id:int)->message.Domain:
        message = self.dataMemory[id]
        return message
    
    def GetAll(self):
        return self.dataMemory
    
    def Save(self, message:message.Domain)-> Tuple(int, Exception):
        self.dataMemory[self.lastId] = message
        self.lastId+=self.lastId

        return (self.lastId, None)