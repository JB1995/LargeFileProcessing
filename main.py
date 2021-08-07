from database.models import DB
from importer import Importer

orm = DB()

importer = Importer(orm)
importer.go()
