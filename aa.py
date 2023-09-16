#restaurant reservation
from datetime import datetime

class reservation():
    def __init__(self, date, amount, table):
        self.date = date
        self.amount = amount
        self.table = table

    def show_info(self):
        print(self.date, self.amount, self.table)



class Aile1(reservation):
    def __init__(self, date, amount, table, cocuk):
        super().__init__(date, amount, table,)
        self.cocuk = cocuk


class Kisi(reservation):
    def __init__(self, date, amount, table, special):
        super().__init__(date, amount, table)
        self.special = special                      

class new(reservation):
    new = 
                   


a1 = Aile1(datetime.now(), 7, 6, 4)
a1.show_info()


ki = Kisi(datetime.now(), 1, 12, "Has A Fancy Hat")
ki.show_info()