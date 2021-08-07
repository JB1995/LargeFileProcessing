from database.models import Products 
from sqlalchemy.dialects.mysql import insert
from sqlalchemy import update

class ProductWriter:
    # Load data into table using upsert: insert if does not exists and updates if exists
    def writeproductsdata(row, writer):
        data = {
            'name':row['name'],
            'sku':row['sku'],
            'description':row['description']
        }
        productsdata = insert(Products).values(data)
        writer.upsert(productsdata, data)