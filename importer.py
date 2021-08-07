from datetime import datetime
from database.basewriter import BaseWriter
from database.productwriter import ProductWriter

import pandas
class Importer:
    def __init__(self, db):
        self.db=db
        self.writer = ProductWriter
        self.basewriter = BaseWriter(self.db)

    def go(self):
        data = pandas.read_csv('dataset\products.csv')
        print (len(data), 'Total records found.')
        starttime = datetime.now()
        print("\n******************************\n Started loading data at: ", starttime)
        for index, row in data.iterrows():
            self.writer.writeproductsdata(row, self.basewriter)
        self.basewriter.commit()
        endtime = datetime.now()
        print("\n Import completed at: ", endtime, "\n******************************")
        print("\n Total table load time: ", endtime-starttime)        