import sqlalchemy as db
from urllib.parse import quote

                        # engine library   user:pass@host     :port/name
# engine = db.create_engine('mysql+pymysql://root:root@localhost:3306/panda')
engine = db.create_engine('mysql+pymysql://root:%s@localhost:3306/panda' % quote('root'))

metadata = db.MetaData()

alaki = db.Table(
    'alaki', 
    metadata,
    db.Column('id', db.Integer(), primary_key=True, autoincrement=True),
    db.Column('name', db.String(255), nullable=False),
    db.Column('family', db.String(255))
)

metadata.create_all(engine)