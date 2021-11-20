from tkinter import *
class Ticket():
    def __init__(self, origin = 'Rasht'
                , destination= 'Tehran',
                departure_date = '1400-11-01',
                ticket_type = 'economy',
                name = 'Test', family = 'Test', age = 30,
                national_code = '1111111111',
                price = 100000
                ):
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.ticket_type = ticket_type
        self.name = name
        self.family = family
        self.age = age
        self.national_code = national_code
        self.price = price
    def get_ticket_info(self):
        return (self.origin, self.destination, self.departure_date, self.ticket_type,
                self.name, self.family, self.age, self.national_code, self.price)