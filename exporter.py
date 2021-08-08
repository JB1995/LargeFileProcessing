from datetime import datetime
from database.aggregate import Aggregate
from sqlalchemy.dialects.mysql import insert
from sqlalchemy import update
from database.models import ProductsNumber
from database.basewriter import BaseWriter
import pandas

class Exporter:
    def __init__(self, db):
        self.db=db
        self.basewriter = BaseWriter(self.db)

    def go(self):
        exportCSV = Aggregate()
        exportCSV.getAggregateCSV()
        
        self.aggregateProducts() 

    def aggregateProducts(self):
        exportstart = datetime.now()
        self.writeAggregate()
        exportdone = datetime.now()
        print ('Exported into database table: ', exportdone-exportstart)
    
    def writeAggregate(self):
        agg = Aggregate()
        data = agg.getAggregateDB()

        print ("-- Writting data")
        for row in data:
            eachrow = data.get(row,{})
            export = insert(ProductsNumber).values(eachrow)
            self.basewriter.upsert(export, eachrow)
            self.basewriter.commit()