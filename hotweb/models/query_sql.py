"""
to define db queries for different sql dialect
"""
from .models import DBConnection
from .models import Models
from .constants import DataTypes
import os
import json
# to get db connection
# read the db configs from the command line
class QueryInterface(Models):
    def __init__(self):
        self.db_ = self.connect_()
        self.db = self.db_[0]
        self.dialect = self.db_[1]["dialect"]
    """

    table_ = F"CREATE TABLE {t_name}("
    end_table = ")"
    line = ""
    for col,attr in args.items():
        """ """for key in args[col].keys():
            line = line+ " "+ " "+ key + args[col][key] + """ """
        line = line+ col_func(args,col,attr)+", \n"
        print(col,attr)
        #table_ += col_func(col[attr],attr)
    print(table_ + line +end_table )
    return table_
    """
    def col_func(self,args,col,attr):
        line = f"{col} "
        for key in args[col].keys():
            if key == "length":
                continue
            if key =="type":
                if "length" in args[col].keys():
                    type_ = f"{DataTypes[self.dialect][args[col]['type']]} ({args[col]['length']})"
                    #type_ = f"{args[col]['type']}({args[col]['length']})" 
                    line = line +" "+ type_ +" "
                else:
                    length = "15"
                    type_ = f"{DataTypes[self.dialect][args[col]['type'].upper()]} ({length})"
                    line = line +" "+ type_ +" "
                continue
            if key.lower() == "allownull":
                if args[col][key]=="False":
                    null = "NOT NULL"
                    line = line +" "+ null
                continue
            if key.lower() == "foreignkey":
                pass
            line = line +" "+ key +" "
        return line
    def connect_(self):
        config_file = os.path.join(os.getcwd(),"models","config.json")
        with open(config_file,"r") as f:
            config = json.load(f)
        
        conn = DBConnection(config["dialect"],db_config=config)
        return [conn,config]
    def createTable(self,dialect,table_name,args):
        if dialect == "mysql":
            sql_ = f"CREATE TABLE {table_name}("
            end_table = ")"
            for col,attr in args.items():
                """for key in args[col].keys():
                line = line+ " "+ " "+ key + args[col][key] + """
                line = line+ self.col_func(args,col,attr)+", \n"
            table = sql_ + line[:-3] +end_table
            curr = self.db.cursor()
            try:
                curr.execute(table)
            except Exception as e:
                print(f"An Error occured while creating the table :: {e}")
        #table_ += col_func(col[attr],attr)
    
    def dropTable(self,table_name):
        sql = f"DROP TABLE IF EXISTS {table_name}"
        try:
            curr = self.db.cursor()
            curr.execute(sql)
        except Exception as e:
            print(f"An error occured while dropping the table :: {e}")
    def addColumn(self,table_name,col):
        sql = f"ALTER TABLE {table_name} ADD COLUMN {col}"
    def dropColumn(self,col):
        pass
    def alterColumn(self,col):
        pass
    def addIndex(self,col):
        pass

queryInterface = QueryInterface()