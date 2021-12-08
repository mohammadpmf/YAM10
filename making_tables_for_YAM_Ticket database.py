from tkinter import *
import sqlalchemy as db
engine = db.create_engine('mysql+pymysql://root:root@localhost:3306/YAM_Ticket') # اگه دیتابیس وجود نداشته باشه، این خط مشکلی ایجاد نمیکنه و متغیر انجین رو میسازه. ولی کانکت شدن بهش ارور میده. دیتابیس باید وجود داشته باشه تا ارور نده.
metadata = db.MetaData()
# ساخت تیبل
tbl_tickets = db.Table(
    'tbl_tickets', # اسم تیبلی که میخوایم بسازه
    metadata,
    db.Column('id', db.Integer(), primary_key=True, autoincrement=True), # یک ستون به این نام و با این ویژگی ها
    db.Column('origin', db.String(45), nullable=False), # یک ستون به این نام و با این ویژگی ها
    db.Column('destination', db.String(45), nullable=False), # یک ستون به این نام و با این ویژگی ها
    db.Column('depart_date', db.Date(), nullable=False), # یک ستون به این نام و با این ویژگی ها
    db.Column('ticket_type', db.String(20), nullable=False), # یک ستون به این نام و با این ویژگی ها
    db.Column('vehicle_type', db.String(20), nullable=False), # یک ستون به این نام و با این ویژگی ها
    db.Column('price', db.String(10), nullable=False) # یک ستون به این نام و با این ویژگی ها
    )
tbl_costumers = db.Table(
    'tbl_costumers', 
    metadata,
    db.Column('id', db.Integer(), primary_key=True, autoincrement=True),
    db.Column('name', db.String(45), nullable=False), # یک ستون به این نام و با این ویژگی ها
    db.Column('family', db.String(45), nullable=False), # یک ستون به این نام و با این ویژگی ها
    db.Column('national_code', db.String(10), nullable=False), # یک ستون به این نام و با این ویژگی ها
    db.Column('age', db.Integer(), nullable=False), # یک ستون به این نام و با این ویژگی ها
    db.Column('id_ticket', db.Integer(), db.ForeignKey(tbl_tickets.c.id), nullable=False)
    )
print(metadata)
metadata.create_all(engine)
