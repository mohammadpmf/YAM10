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
        self.top.grab_set()
        self.top.geometry('400x400')
        self.top.title('Enrolling ticket')
        Label(self.top, text='Origin: ').        grid(row=1, column=1)
        Label(self.top, text='Destination: ').   grid(row=2, column=1)
        Label(self.top, text='Departure Date: ').grid(row=3, column=1)
        Label(self.top, text='Type: ').          grid(row=4, column=1)
        Label(self.top, text='Price: ').         grid(row=5, column=1)
        self.sv_origin = StringVar()
        self.sv_origin.set('Rasht')
        self.sv_destination = StringVar()
        self.sv_destination.set('Tehran')
        self.sv_type = StringVar()
        print(self.sv_type.get())
        self.iv_price = IntVar()
        self.iv_price.set(1000)
        Entry(self.top, textvariable=self.sv_origin).                         grid(row=1, column=2, sticky='news')
        Entry(self.top, textvariable=self.sv_destination).                    grid(row=2, column=2, sticky='news')
        Entry(self.top, textvariable=self.iv_price).                          grid(row=5, column=2, sticky='news')
        self.ticket_type = ttk.Combobox(self.top, values=types, state='readonly')
        self.ticket_type.current(0)
        self.ticket_type.grid(row=4, column=2, sticky='news')
        # departure_date = Entry(self.top, textvariable=sv_destination)
        # departure_date.grid(row=3, column=2)
        self.departure_date = tkcalendar.DateEntry(self.top, selectmode = 'day', year = 2021, month = 12,day = 1)
        self.departure_date.grid(row=3, column=2, sticky='news')
        Button(self.top, text='Register', command=self.register).grid(row=6, column=1, sticky='news')
        Button(self.top, text='Cancel', command=self.top.destroy).grid(row=6, column=2, sticky='news')
    def register(self):
        print(self.sv_origin.get())
        print(self.sv_destination.get())
        print(self.iv_price.get())
        print(self.ticket_type.get())
        print(self.departure_date.get())
