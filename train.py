from ticket import *
import tkinter.ttk
from tkinter import ttk
from tkinter import messagebox
import sqlalchemy as db

class Train(Ticket):

    def __init__(self
                 ,origin='Rasht'
                 ,destination = 'Tehran'
                 ,departure_date= '1400_11_01'
                 ,ticket_type='economy'
                 ,name="Test",family="Test",age=30
                 ,national_cod='123456789'
                 ,price= 100000,
                 id_ticket= 0):

        self.origin=origin
        self.destination=destination
        self.departure_date=departure_date
        self.ticket_type=ticket_type
        self.name=name
        self.family=family
        self.age=age
        self.national_cod=national_cod
        self.price=price
        self.id_ticket = id_ticket

        self.t=Tk()
        self.t.title('Train ticket')
        self.subwindow = Toplevel(self.t)
        self.subwindow.title('Information')
        self.anotherwin = Toplevel(self.t)
        self.anotherwin.title('Options')
        self.theotherwin = Toplevel(self.t)
        self.anotherwin.withdraw()
        self.subwindow.withdraw()
        self.theotherwin.withdraw()

        self.var = StringVar()
        self.var2 = StringVar()

    def check_age(self):
        if int(self.spinbox.get()) < 15:
            self.var2.set("You're too young to travel alone")
            self.spinbox2['state'] = 'readonly'
        else:
            self.spinbox2['state'] = 'disabled'

    def make_form(self):
        def next1():
            self.t.withdraw()
            self.anotherwin.withdraw()
            self.subwindow.deiconify()
            self.theotherwin.withdraw()
        def next2():
            self.t.withdraw()
            self.subwindow.withdraw()
            self.anotherwin.deiconify()
            self.theotherwin.withdraw()
        def next3():
            self.t.withdraw()
            self.subwindow.withdraw()
            self.anotherwin.withdraw()
            self.theotherwin.deiconify()

        self.engine = db.create_engine('mysql+pymysql://root:root@localhost:3306/YAM_Ticket')
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.tbl_tickets = db.Table("tbl_tickets", self.metadata, autoload=True, autoload_with=self.engine)
        self.tbl_costumers = db.Table("tbl_costumers", self.metadata, autoload=True, autoload_with=self.engine)

        Label(self.t, text='Origin').grid(row=1, column=1, padx=20, pady=20)
        Label(self.t, text='Destination').grid(row=2, column=1)
        Label(self.t, textvariable=self.var).grid(row=5, column=1)
        Label(self.subwindow, text='Name').grid(row=1, column=1, padx=20, pady=20)
        Label(self.subwindow, text='Family name').grid(row=2, column=1)
        Label(self.subwindow, text='ID').grid(row=3, column=1)
        Label(self.subwindow, text='Age').grid(row=4, column=1)
        Label(self.subwindow, textvariable=self.var2).grid(row=5, column=1)
        Label(self.subwindow, text='parent_age').grid(row=6, column=1)
        Label(self.anotherwin, text='Ticket type').grid(row=4, column=1)
        Label(self.theotherwin, text='Price').grid(row=1, column=1, sticky='news')
        Label(self.anotherwin, text='Year').grid(row=1, column=1)
        Label(self.anotherwin, text='Month').grid(row=2, column=1)
        Label(self.anotherwin, text='Day').grid(row=3, column=1)
        


        box = tkinter.ttk.Combobox(self.t , state='readonly')
        box.grid(row=1, column=2)
        box['values'] = ('Isfahan','Dubai','Amsterdam','Washington','Moscow','Toronto','Berlin','Rome','Texas', 'other')
        box.current(0)

        box2 = tkinter.ttk.Combobox(self.t, state='readonly')
        box2.grid(row=2, column=2)
        box2['values'] = ('Mashhad','Istanbul','Pris','Hawii','Califotnia','Kazan','Vancouver','Venice', 'other')
        box2.current(0)
        
        c4 = tkinter.ttk.Combobox(self.anotherwin, values=['first class', 'economy', 'business class'], state='readonly')
        c4.grid(row=4, column=2, columnspan=4)
        
        e1 = Entry(self.t)
        e1.grid(row=1, column=3)
        e1.insert(0, box['values'][0])
        e1['state'] = 'readonly'
        e2 = Entry(self.t)
        e2.insert(0, box2['values'][0])
        e2['state'] = 'readonly'
        e2.grid(row=2, column=3)
        e_name = Entry(self.subwindow)
        e_name.grid(row=1, column=2)
        e_family = Entry(self.subwindow)
        e_family.grid(row=2, column=2)
        e_nt_cod = Entry(self.subwindow)
        e_nt_cod.grid(row=3, column=2)



        def other1(event):
            if str(event.widget).endswith('combobox'):
                if box.get() == 'other':
                    e1['state'] = 'normal'
                    e1.delete(0, END)
                else:
                    e1['state'] = 'normal'
                    e1.delete(0, END)
                    e1.insert(0, box.get())
                    e1['state'] = 'readonly'
            if str(event.widget).endswith('combobox2'):
                if box2.get() == 'other':
                    e2['state'] = 'normal'
                    e2.delete(0, END)
                else:
                    e2['state'] = 'normal'
                    e2.delete(0, END)
                    e2.insert(0, box2.get())
                    e2['state'] = 'readonly'
        self.t.bind('<<ComboboxSelected>>', other1)

        self.spinbox = Spinbox(self.subwindow, from_=1, to=120, state='readonly', command=self.check_age)
        self.spinbox.grid(row=4, column=2)
        self.spinbox2 = Spinbox(self.subwindow, from_=20, to=120, state='disabled')
        self.spinbox2.grid(row=6, column=2)

        spin_year = Spinbox(self.anotherwin,from_=1920, to=2120)
        spin_year.grid(row=1, column=2)
        spin_month = Spinbox(self.anotherwin,from_=1, to=12)
        spin_month.grid(row=2, column=2)
        spin_day = Spinbox(self.anotherwin,from_=1, to=31)
        spin_day.grid(row=3, column=2)

        def calculate_payment():
            price = 1000
            if self.spinbox.get() < 15:
                price -= 150
            if self.spinbox2.get() >= 20:
                price += 1200
            if c4.get() == 'first class':
                price += 2000
            elif c4.get() == 'business class':
                price += 1500
            elif c4.get() == 'economy':
                price += 1000
            else:
                price += 500
            lbl_payment['text'] = int(price)
        lbl_payment = Label(self.theotherwin, text=calculate_payment)
        lbl_payment.grid(row=1, column=1, sticky='news')

        def return_date():
            date = f'{spin_year.get()}-{spin_month.get()}-{spin_day.get()}'
            return date

        def show_result():
            ticket_type = IntVar()
            def clicked(event):
                # item = treev.identify('item',event.x,event.y)
                curItem = treev.focus()
                self.price = treev.item(curItem)['values'][-1]
                try:
                    self.id_ticket = int(treev.item(curItem)['text'][1:3])
                except:
                    try:
                        self.id_ticket = int(treev.item(curItem)['text'][1])
                    except:
                        print('bad id format while reading id')

                t2.destroy()
                btn_buy['state'] = 'normal'

            t2 = Toplevel(self.anotherwin)
            treev = ttk.Treeview(t2, height=5, selectmode ='browse', columns=("1", "2", "3","4","5"), show='headings')
            treev.grid(row=1, column=1)

            vertical_scrlbar = ttk.Scrollbar(t2,orient ="vertical",command = treev.yview)
            vertical_scrlbar.grid(row=1, column=2, sticky='ns')

            treev.configure(yscrollcommand = vertical_scrlbar.set)

            treev.column("1", width=100, anchor ='c')
            treev.column("2", width=150, anchor ='c')
            treev.column("3", width=150, anchor ='c')
            treev.column("4", width=150, anchor ='c')
            treev.column("5", width=100, anchor ='c')

            treev.heading("1", text ="origin")
            treev.heading("2", text ="destination")
            treev.heading("3", text ="departure_date")
            treev.heading("4", text ="ticket_type")
            treev.heading("5", text ="price")

            def return_ticket():

                if c4.get() == 'economy':
                    return 'economy'
                elif c4.get() == 'first class':
                    return 'first class'
                elif c4.get() == 'business class':
                    return 'business class'
            def return_box():
                if box.get() != 'other':
                    return box.get()
                else:
                    return e1.get()
            def return_box2():
                if box2.get() != 'other':
                    return box2.get()
                else:
                    return e2.get()
            print(return_box(), return_box2(), return_date(), return_ticket())
            query = db.select(self.tbl_tickets).where(
                self.tbl_tickets.c.origin == return_box(),
                self.tbl_tickets.c.destination == return_box2(),
                self.tbl_tickets.c.depart_date == return_date(),
                self.tbl_tickets.c.ticket_type == return_ticket())

            result = self.connection.execute(query)
            for i in result:
                treev.insert("", 'end', text=i, values=(i[1], i[2], i[3], i[4], i[6]))

            treev.bind('<Double-1>', clicked)

        def buy():
    
            db_date = return_date()
            query = db.insert(self.tbl_costumers).values(
                {
                    
                    'name': e_name.get(),
                    'family': e_family.get(),
                    'national_code': e_nt_cod.get(),
                    'age': self.spinbox.get(),
                    'id_ticket': self.id_ticket
                })
            try:
                self.connection.execute(query)
                messagebox.showinfo('Success', 'Ticket Successfully added to DB')
            except:
                messagebox.showwarning('warning', 'Bad date format!')        


        Button(self.t, text='next', command=next1).grid(row=10, column=1)
        Button(self.subwindow, text='next', command=next2).grid(row=10, column=1)
        btn_buy = Button(self.anotherwin, text='Buy', command=next3, state='disabled')
        btn_buy.grid(row=10, column=1)
        btn_show = Button(self.anotherwin, text="show the price", command=show_result, activebackground="#90CAF9")
        btn_show.grid(row=11, column=1)