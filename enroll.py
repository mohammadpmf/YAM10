import tkinter
import tkcalendar
from ticket import *
from tkinter import ttk

types = ['economy', 'business class', 'first class']

class Enroll():
    def __init__(self, root, ticket):
        self.root = root
        self.origin = ticket.origin
        self.destination = ticket.destination
        self.departure_date = ticket.departure_date
        self.ticket_type = ticket.ticket_type
        self.price = ticket.price
        self.top = Toplevel(self.root)
        self.top.geometry('400x400')
        self.top.title('Enrolling ticket')
        Label(self.top, text='Origin: ').        grid(row=1, column=1)
        Label(self.top, text='Destination: ').   grid(row=2, column=1)
        Label(self.top, text='Departure Date: ').grid(row=3, column=1)
        Label(self.top, text='Type: ').          grid(row=4, column=1)
        Label(self.top, text='Price: ').         grid(row=5, column=1)
        sv_origin = StringVar()
        sv_destination = StringVar()
        sv_type = StringVar()
        sv_type.set(types[0])
        iv_price = IntVar()
        Entry(self.top, textvariable=sv_origin).                         grid(row=1, column=2)
        Entry(self.top, textvariable=sv_destination).                    grid(row=2, column=2)
        Entry(self.top, textvariable=iv_price).                          grid(row=5, column=2)
        ttk.Combobox(self.top, values=types, textvariable=sv_type, state='readonly').grid(row=4, column=2)
        departure_date = Entry(self.top, textvariable=sv_destination)
        departure_date.grid(row=3, column=2)
        # departure_date = tkcalendar.Calendar(self.top, selectmode = 'day', year = 2021, month = 12,day = 1)
        # departure_date.grid(row=3, column=2)

