from operator import and_
import sqlalchemy as db
from tkcalendar import DateEntry

import tkinter as tk
from tkinter import StringVar, ttk
from datetime import datetime

from sqlalchemy.sql.expression import column, text


def set_pa():
    for person, present in zip(cb_list, cb_var):
        q = db.insert(pa).values({
            'date': cal.get_date(),
            's_id': person[0],
            'present': present.get()
        })
        connection.execute(q)

def update_class_list():
    cb_list.clear()
    cb_var.clear()
    select_all()
    for r, op in enumerate(cb_list):
        var = tk.BooleanVar(root, False)
        cb = tk.Checkbutton(canvas, variable=var, text=op[1], relief='ridge')
        cb.grid(row=r+1, column=0, sticky="w")
        cb_var.append(var)


def select_all():
    query = db.select(student)
    result = connection.execute(query)
    for r in result:
        cb_list.append(r)

def register():
    query = db.insert(student).values({'fullname': fullname_frame1.get()})
    connection.execute(query)
    fullname_frame1.set('')
    update_class_list()

# ############################################ SQLALCHEMY
engine = db.create_engine('mysql+pymysql://root:root@localhost:3306/panda')
connection = engine.connect()
metadata = db.MetaData()
student = db.Table("student", metadata, autoload=True, autoload_with=engine)
pa = db.Table("pa", metadata, autoload=True, autoload_with=engine)
#########################################################

root = tk.Tk()

# ############################################## NoteBook
notebook = ttk.Notebook(root)
frame0 = tk.Frame(notebook)
frame1 = tk.Frame(notebook)
frame2 = tk.Frame(notebook, width=300,height=300)
notebook.add(frame0, text='test')
notebook.add(frame1, text='Register Student')
notebook.add(frame2, text='Present&Absent')
notebook.grid(row=0, column=0)

# #######################################################

def minsert():
    query = db.insert(alaki).values(
        {
            'name': t1.get(),
            'family': t1.get()+'i',
        })
    connection.execute(query)
def mupdate():
    query = db.update(alaki).values(
        {
            'name': t2.get() + 'updateddd',
            'family': t2.get()+' updateddd 2',
        }).where(alaki.c.id==1)
    connection.execute(query)
def melete():
    query = db.delete(alaki).where(alaki.c.name==t3.get())
    connection.execute(query)
def mow():
    query = db.select(alaki).where(alaki.c.name==t4.get())
    result = connection.execute(query)
    for i in result:
        print(i)


tk.Button(frame0, text='insert', command=minsert).pack()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
tk.Entry(frame0, textvariable=t1).pack()
tk.Button(frame0, text='update', command=mupdate).pack()
tk.Entry(frame0, textvariable=t2).pack()
tk.Button(frame0, text='delete', command=melete).pack()
tk.Entry(frame0, textvariable=t3).pack()
tk.Button(frame0, text='show', command=mow).pack()
tk.Entry(frame0, textvariable=t4).pack()

# ###################################### Register Student
tk.Label(frame1, text='Student Name').grid(row=0, column=0)
fullname_frame1 = tk.StringVar()
tk.Entry(frame1, textvariable=fullname_frame1).grid(row=0, column=1)
tk.Button(frame1, text='Register', command=register).grid(row=1, column=0)
# #######################################################

# ################################ Absent/Present Student

alaki = db.Table("alaki", metadata, autoload=True, autoload_with=engine)

canvas = tk.Canvas(frame2, scrollregion=(0,0,500,500))
canvas.config(width=300,height=300)
canvas.grid(row=0, column=0)

vbar = ttk.Scrollbar(frame2, orient=tk.VERTICAL)
vbar.grid(row=0, column=1, sticky='sn')
canvas.config(yscrollcommand=vbar.set)
vbar.config(command=canvas.yview)

n = datetime.now()
cal = DateEntry(canvas, width=12, year=n.year, date_pattern='y-mm-dd')
cal.config(background='darkblue', foreground='white', borderwidth=2)
cal.grid(row=0, column=0)

cb_list = [] 
cb_var = [] 
update_class_list()

tk.Button(canvas, text='Set', command=set_pa).grid(row=len(cb_list)+1, column=0)

# #######################################################


root.mainloop()