from database.models import DB
from importer import Importer
from exporter import Exporter

orm = DB()

importer = Importer(orm)
importer.go()

exporter = Exporter(orm)
exporter.go()