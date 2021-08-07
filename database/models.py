import os
import mysql.connector
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

# Defining database connections
class DB:
    def __init__(self):
        # self.engine = db.create_engine('mysql+mysqlconnector://root:'+os.environ['MYSQL_ROOT_PASSWORD']+'@'+os.environ['DB_CONTAINER_NAME']+'/metrics')
        self.engine = db.create_engine('mysql+mysqlconnector://Dealersocket:metrics123@localhost:3307/demo')
        self.conn = self.engine.connect()
        
        Session = db.orm.sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()
    
    def session(self):
        return self.session
    
    def engine(self):
        return self.engine
    
    def connection(self):
        return self.conn
    
orm = DB()
engine = orm.engine
session = orm.session
Base = declarative_base()

# Creating Products table
class Products(Base):
  __tablename__ = 'Products'
  
  name = db.Column(db.String(length=500))
  sku = db.Column(db.String(length=500), primary_key=True)
  description = db.Column(db.String(length=500))
  
  def __repr__(self):
    return "{0} - {1}".format(self.sku, self.name)

Base.metadata.create_all(engine)