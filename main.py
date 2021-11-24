from ticket import Ticket
from tkinter import *
from tkinter import ttk, messagebox
from enroll import Enroll

def enter():
    if username.get() == 'admin' and password.get() == 'admin':
        t = Ticket()
        e = Enroll(root, t)
    else:
        messagebox.showerror('', 'Wrong password')
root = Tk()
root.geometry('600x300')
root.title('Ticket Reservation')
notebook = ttk.Notebook(root)
tab_manager = Frame(notebook)
tab_costumer = Frame(notebook)
notebook.add(tab_manager,text='Management')
notebook.add(tab_costumer,text='Buy a Ticket')
notebook.grid(row=0, column=0)
lbl_cnf ={
    'fg':'#770000',
    'bg':'#777777',
    'font':('Tahoma', 12, 'italic')
}
btn_cnf ={
    'fg':'#008800',
    'bg':'#222222',
    'font':('Tahoma', 12, 'italic')
}
Label(tab_manager, text='Username:', cnf=lbl_cnf).grid(row=1, column=1)
Label(tab_manager, text='Password:', cnf=lbl_cnf).grid(row=2, column=1)
username = StringVar()
password = StringVar()
username.set('admin')
password.set('admin')
Entry(tab_manager, textvariable=username).grid(row=1, column=2)
Entry(tab_manager, textvariable=password, show='*').grid(row=2, column=2)
Button(tab_manager, text='OK', command=enter, cnf=btn_cnf).grid(row=3, column=1, columnspan=2, sticky='news')

def buy_airplane_ticket():
    pass
def buy_train_ticket():
    pass
def buy_ship_ticket():
    pass
def buy_bus_ticket():
    pass
Button(tab_costumer, text='Buy an airplane ticket'
        , command=buy_airplane_ticket).grid(row=1, column=1, sticky='news')
Button(tab_costumer, text='Buy a train ticket'
        , command=buy_train_ticket).grid(row=2, column=1, sticky='news')
Button(tab_costumer, text='Buy an ship ticket'
        , command=buy_ship_ticket).grid(row=3, column=1, sticky='news')
Button(tab_costumer, text='Buy an bus ticket'
        , command=buy_bus_ticket).grid(row=4, column=1, sticky='news')

mainloop()