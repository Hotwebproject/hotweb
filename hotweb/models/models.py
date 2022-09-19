# models functions

class Models:
    def __init__(self,model_name,db="",dialect=""):
        self.model_name =model_name
        self.cursor = db
    # validate if the user key_queries are accurate
    """
    check if the key value pairs of queries match eg if a field is null but
    its required thru model declaration then raise an error
    """
    def _validate_input(self):
        pass
    # args is a dict of model fields
    def create(self,args):
        pass
    # used to unpack the args it returns the col names
    def _unpack_args(self,args):
        pass
    def findOne(self,arg):
        pass
    
    def findAll(self,arg):
        pass
    # to delete
    def destroy(self,arg):
        pass
    
    def findAndUpdate(self,args):
        pass
    # used to create fields for the db, not used to create tables created thru migrations
    def init(self,model_name,args):
        query = "create table query"
        # table_fields = ""
        # len_args = len(args)
        # sql = ""
    
    def _gettype_(self,arg):
        if len(arg)==0:
            return False
        if isinstance(arg,str):
            return "%s"
        elif isinstance(arg,int):
            return "%d"
    """
    hasOne and has Many are used to define associations
    model arg --> is a string name for a Model
    """
    def hasOne(self,model,options={}):
        pass
    
    def hasMany(self,model,options={}):
        pass

class DBConnection:
    """
    dialect defines the type of sql database
    args define a dictionary of db configurations eg host,port,password
    try to connect to db else raise an error
    -->install the driver for the selected dialect except for sqlite which is built in
    """
    
    def __init__(self,dialect,**kwargs):
        self.dialect = dialect
        self.kwargs = kwargs
    
    def connect(self):
        # call appropriate method based on provided dialect
        if self.dialect.lower() =="sqlite" or self.dialect.lower() =="sqlite3":
            self.sqlite_db()
        elif self.dialect.lower() =="mysql":
            pass
        pass
    def sqlite_db(self):
        import sqlite3
        # get db name from the kwargs

        conn = sqlite3.connect(self.kwargs)
        return conn
    
    def mysql_db(self):
        pass
    def postgress_db(self):
        pass
    def mssql_db(self):
        pass
    
    # other dbs


class Models_Migrate:
    pass