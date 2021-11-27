from tkinter import*
from ticket import *
from tkinter import ttk
from tkinter import messagebox
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
    def make_form(self):

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
        combo_origin = ttk.Combobox(t, values=('A', 'B', 'C'))
        combo_origin.place(x=370, y=100, width=100, height=30)
        lbl_destination = Label(t, text="destination", fg="#2196F3")
        lbl_destination.place(x=250, y=70, width=100, height=30)
        combo_destination = ttk.Combobox(t, values=('A', 'B', 'C'))
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



        btn_show = Button(t, text="show the price", command=show_price, activebackground="#90CAF9")
        btn_show.place(x=15, y=145, width=220, height=15)
        e_price = Entry(t)
        e_price.place(x=60, y=165, width=175, height=20)
        lbl_price = Label(t, text="price :", bg="#2196F3", fg="white")
        lbl_price.place(x=15, y=165, width=40, height=20)
        mainloop()

