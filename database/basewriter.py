from sqlalchemy.dialects.mysql import insert
class BaseWriter:    
    def __init__(self, db):
        self.db = db
        self.connection = db.connection()
    
    def upsert(self, insert, data):
        upsert = insert.on_duplicate_key_update(data)
        self.connection.execute(upsert)
    
    def commit(self):
        self.db.session.commit()