from tkinter import*
from ticket import *
from tkinter import ttk
from tkinter import messagebox
import sqlalchemy as db
cities = ['Rasht', 'Tehran', 'Shiraz', 'Isfahan', 'Mashhad']

class Ship():
    def __init__(self, origin='Rasht'
                 ,destination = 'Tehran'
                 ,departure_date= '1400_11_01'
                 ,ticket_type='economy'
                 ,name="Test",family="Test",age=30
                 ,national_cod='123456789'
                 ,price= 100000
                 ):
        self.origin=origin
        self.destination=destination
        self.departure_date=departure_date
        self.ticket_type=ticket_type
        self.name=name
        self.family=family
        self.age=age
        self.national_cod=national_cod
        self.price=price
        self.id_ticket = 0
    def make_form(self):
        self.engine = db.create_engine('mysql+pymysql://root:root@localhost:3306/YAM_Ticket')
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.tbl_tickets = db.Table("tbl_tickets", self.metadata, autoload=True, autoload_with=self.engine)
        self.tbl_costumers = db.Table("tbl_costumers", self.metadata, autoload=True, autoload_with=self.engine)

        t = Toplevel()
        t.geometry("480x200")
        t.title('ship reservation')
        t.resizable(0, 0)
        f1 = Frame(t, bg="#2196F3")
        f1.place(x=0, y=0, width=480, height=70)
        f2 = Frame(t, bg="#2196F3")
        f2.place(x=10, y=140, width=230, height=50)
        lbl_age = Label(f1, text="age", bg="#2196F3", fg="white")
        lbl_age.place(x=10, y=0, width=100, height=30)
        s_age = Spinbox(f1, from_=1, to=200)
        s_age.place(x=10, y=30, width=100, height=30)
        lbl_nt_cod = Label(f1, text="national cod", bg="#2196F3", fg="white")
        lbl_nt_cod.place(x=130, y=0, width=100, height=30)
        e_nt_cod = Entry(f1)
        e_nt_cod.place(x=130, y=30, width=100, height=30)
        lbl_family = Label(f1, text="family", bg="#2196F3", fg="white")
        lbl_family.place(x=250, y=0, width=100, height=30)
        e_family = Entry(f1)
        e_family.place(x=250, y=30, width=100, height=30)
        lbl_name = Label(f1, text="name", bg="#2196F3", fg="white")
        lbl_name.place(x=370, y=0, width=100, height=30)
        e_name = Entry(f1)
        e_name.place(x=370, y=30, width=100, height=30)
        lbl_origin = Label(t, text="origin", fg="#2196F3")
        lbl_origin.place(x=370, y=70, width=100, height=30)
        combo_origin = ttk.Combobox(t, values=(cities))
        combo_origin.place(x=370, y=100, width=100, height=30)
        lbl_destination = Label(t, text="destination", fg="#2196F3")
        lbl_destination.place(x=250, y=70, width=100, height=30)
        combo_destination = ttk.Combobox(t, values=(cities))
        combo_destination.place(x=250, y=100, width=100, height=30)
        lbl_departure_date = Label(t, text="departure date", fg="#2196F3")
        lbl_departure_date.place(x=70, y=70, width=100, height=30)
        spin_month = Spinbox(t, from_=1, to=12)
        spin_month.place(x=95, y=100, width=55, height=30)
        spin_year = Spinbox(t, from_=1920, to=2120)
        spin_year.place(x=35, y=100, width=60, height=30)
        spin_day = Spinbox(t, from_=1, to=31)
        spin_day.place(x=150, y=100, width=50, height=30)
        lbl_ticket_type = Label(t, text="ticket type", fg="#2196F3")
        lbl_ticket_type.place(x=310, y=140, width=100, height=30)
        ticket_type = IntVar()
        rb1 = Radiobutton(t, text='economy', variable=ticket_type, value=1, fg="#2196F3")
        rb2 = Radiobutton(t, text='first class', variable=ticket_type, value=2, fg="#2196F3")
        rb3 = Radiobutton(t, text='business', variable=ticket_type, value=3, fg="#2196F3")
        ticket_type.set(3)
        rb1.place(x=400, y=160, width=70, height=30)
        rb2.place(x=330, y=160, width=70, height=30)
        rb3.place(x=260, y=160, width=70, height=30)
        def return_date():
                date=f'{spin_year.get()}-{spin_month.get()}-{spin_day.get()}'
                return date
        def show_result():
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
                print(treev.item(curItem)['text'])
                print(self.id_ticket)
                # print(treev.item(curItem)['values'][-1])
                # print (treev.item(curItem))
                # print("you clicked on", treev.item(item,"text"))
                e_price.delete(0, END)
                e_price.insert(0, str(self.price)+ "$")
                btn_buy['state'] = 'normal'
                t2.destroy()
            t2 = Toplevel(t)
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
            def return_ticket_type():
                if ticket_type.get() == 1:
                    return 'economy'
                elif ticket_type.get() == 2:
                    return 'first class'
                elif ticket_type.get()==3:
                    return 'business class'
                
            query = db.select(self.tbl_tickets).where(
                self.tbl_tickets.c.origin == combo_origin.get(),
                self.tbl_tickets.c.destination==combo_destination.get(),
                self.tbl_tickets.c.depart_date==return_date(),
                self.tbl_tickets.c.ticket_type==return_ticket_type()
            )
            result = self.connection.execute(query)
            for i in result:
                treev.insert("", 'end', text=i, values=(i[1], i[2], i[3], i[4], i[6]))

            treev.bind('<Double-1>', clicked)

        def show_price():
            last_price=1
            swcond_price=1
            age=int(s_age.get())
            main_price=10
            if ticket_type.get() == 1:
                second_price=main_price
                if age>2 and age<16:
                    last_price=second_price/2
                elif age > 15:
                    last_price=second_price
            elif ticket_type.get()==2:
                second_price = main_price*2
                if age > 2 and age < 16:
                    last_price = second_price / 2
                elif age > 15:
                    last_price = second_price
            elif ticket_type.get()==3:
                second_price = main_price*3
                if age > 2 and age < 16:
                    last_price = second_price / 2
                elif age > 15:
                    last_price = second_price
            e_price.delete(0, END)
            e_price.insert(0, str(last_price) + "$")
            # print(last_price)

        def buy():
            query = db.insert(self.tbl_costumers).values(
            {
                'name': e_name.get(),
                'family': e_family.get(),
                'national_code': e_nt_cod.get(),
                'age': s_age.get(),
                'id_ticket': self.id_ticket,
            })
            try:
                self.connection.execute(query)
                messagebox.showinfo('Success', 'Ticket Successfully added to DB')
            except:
                messagebox.showwarning('warning', 'something went wrong')

        btn_show = Button(t, text="show the price", command=show_result, activebackground="#90CAF9")
        btn_show.place(x=15, y=145, width=220, height=15)
        btn_buy = Button(t, text="Buy this ticket", command=buy,  activebackground="#90CAF9", state='disabled')
        btn_buy.place(x=0, y=145, width=100, height=15)
        e_price = Entry(t)
        e_price.place(x=60, y=165, width=175, height=20)
        lbl_price = Label(t, text="price :", bg="#2196F3", fg="white")
        lbl_price.place(x=15, y=165, width=40, height=20)

        mainloop()

