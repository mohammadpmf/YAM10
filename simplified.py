import sqlalchemy as db

import tkinter as tk
from tkinter import StringVar

engine = db.create_engine('mysql+pymysql://root:root@localhost:3306/jjjjj')
connection = engine.connect()
metadata = db.MetaData()
alaki = db.Table("alaki", metadata, autoload=True, autoload_with=engine)


def insert():
    query = db.insert(alaki).values(
        {
            'name': t1.get(),
            'family': t1.get()+'i',
        })
    connection.execute(query)
def update():
    query = db.update(alaki).values(
        {
            'name': t2.get() + 'updated',
            'family': t2.get()+' updated 2',
        }).where(alaki.c.name==t2.get())
    connection.execute(query)
def delete():
    query = db.delete(alaki)
    connection.execute(query)
def show():
    query = db.select(alaki).where(alaki.c.name == t4.get())
    result = connection.execute(query)
    for i in result:
        print(i)


root = tk.Tk()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
tk.Button(root, text='insert', command=insert).pack()
tk.Entry(root, textvariable=t1).pack()
tk.Button(root, text='update', command=update).pack()
tk.Entry(root, textvariable=t2).pack()
tk.Button(root, text='delete', command=delete).pack()
tk.Entry(root, textvariable=t3).pack()
tk.Button(root, text='show', command=show).pack()
tk.Entry(root, textvariable=t4).pack()

root.mainloop()