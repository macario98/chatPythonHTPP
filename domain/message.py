import datetime


class Domain:
    From:int
    To:int
    Body:str
    Datetime:datetime.datetime
    def __init__(self,
                 From:int=0,
                 To:int=0,
                 Body:str="",
                 Dt:datetime=datetime.datetime.utcnow()
                 ) -> None:
        self.From=From
        self.To = To
        self.Body = Body
        self.Datetime = Dt