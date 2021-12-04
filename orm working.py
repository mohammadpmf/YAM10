from tkinter import *
import sqlalchemy as db

#                         engine library   user:pass@host     :port/db_name     # host: جایی که دیتابیسمون قرار داره
engine = db.create_engine('mysql+pymysql://root:root@localhost:3306/sample') # اگه دیتابیس وجود نداشته باشه، این خط مشکلی ایجاد نمیکنه و متغیر انجین رو میسازه. ولی کانکت شدن بهش ارور میده. دیتابیس باید وجود داشته باشه تا ارور نده.
# engine = db.create_engine('mysql+mysqlconnector://root:root@localhost:3306/sample') # مای اس کیو ال کانکتور، نقطه اش رو نباید بذاریم. البته آقای بخشنده میگفت رو لینوکس یا ویندوز مشکل داره به خاطر همین پای مای اس کیو ال رو ترجیح میداد.
# print(engine)
# connection = engine.connect() # ساخت کانکشدن هم لازم نیست. برای تست کردن خوبه ولی. میتونیم ببینیم که کانکت شده یا نه. اگه نشه ارور میده و میشه با اکسپت هندلش کرد و فهمید که کانکت شده یا نه و اگر هم وصل بشه که شده دیگه مشکلی نیست.
# print(connection)
metadata = db.MetaData()
print(metadata)

# ساخت تیبل
student = db.Table(
    'student', # اسم تیبلی که میخوایم بسازه
    metadata,
    db.Column('id', db.Integer(), primary_key=True, autoincrement=True), # یک ستون به این نام و با این ویژگی ها
    db.Column('name', db.String(255), nullable=False) # یک ستون به این نام و با این ویژگی ها
    )
print(metadata)
present_absent = db.Table(
    'pres_abs', 
    metadata,
    db.Column('id', db.Integer(), primary_key=True, autoincrement=True),
    db.Column('date', db.Date(), nullable=False),
    db.Column('s_id', db.Integer(), db.ForeignKey(student.c.id), nullable=False),
    db.Column('present', db.Boolean(), nullable=False)
    )
print(metadata)
metadata.create_all(engine)
# metadata.drop_all(engine)
