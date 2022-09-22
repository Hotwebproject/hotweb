"""
to define db queries for different sql dialect
"""
from models import DBConnection
# to get db connection
# read the db configs from the command line
class QueryInterface:
    def __init__(self,db_instance):
        self.db = db_instance
    
    def createTable(self,table_name,attrs):
        pass
    
    def dropTable(self,table_name):
        pass
    def addColumn(self,col):
        pass
    def dropColumn(self,col):
        pass
    def alterColumn(self,col):
        pass

queryInterface = QueryInterface("test_db_args")