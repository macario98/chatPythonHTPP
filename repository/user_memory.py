from ..domain import user
from typing import Dict, Tuple

class Repository:
    dataMemory: Dict[int, user.Domain]
    lastid: int

    def __init__(self) -> None:
        self.dataMemory = {}
        self.lastid = 0

    def Get(self, id:int) -> user.Domain:
        user = self.dataMemory[id]
        return user
    
    def GetAll(self):
        return self.dataMemory
    
    def Save(self, user:user.Domain) -> Tuple(int, Exception):
        self.dataMemory[self.lastid] = user
        self.lastid+=self.lastid

        return (self.lastid, None)

        