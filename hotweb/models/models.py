# models functions

class Models:
    def __init__(self,model_name,db=None,dialect=""):
        self.model_name =model_name
        self.db = db
    # validate if the user key_queries are accurate
    """
    check if the key value pairs of queries match eg if a field is null but
    its required thru model declaration then raise an error
    ---------------------------------------------------------------------------
    also check if the datatypes are the same
    ---------------------------------------------------------------------------
    """
    def _validate_input(self,arg):
        for col,attributes in self.table_fields.items():
            # attributes is a dictionary
            if "allowNull" in attributes.keys():
                if col["allowNull"] == False and col not in arg.keys():
                    # raise field required error
                    pass

                elif col["allowNull"] == False and col not in arg.keys():
                    # raise field canot be empty error
                    pass
    def _validate_input_type(self,arg):
        pass
    # args is a dict of model fields
    """
    The create function handles insertion of data into the database
    It unpacks col values from the supplied args and validate the input to check if any
    required field is required or missing
    """
    def create(self,args,many={}):
        # many will handle executemany()
        db = self.db
        curr = db.cursor()
        len_args = len(args.keys())
        plcaholders= "("+"%,"*(len_args-1)+"%"+")"
        cols = "("
        for col in args.keys():
            cols =cols + col+","
        values = tuple(args.values())
        print(tuple(values))
        query = f"INSERT INTO {self.model_name}" +cols[:-1] +")" +" VALUES"+ plcaholders
        try:
            curr.execute(query,values)
            db.commit()
        except Exception as e:
            print(e)
        finally:
            db.close()
        print(query)
    # used to unpack the args it returns the col names
    def _unpack_args(self,args):
        pass
    # sketch of the query
    def findOne(self,args):
        if not self.db:
            # raise no db connection estabilished error
            pass
        where_placeholders = ""
        values = []
        for k,v in args.items():
            if k.lower() == "where":
                for col,val in args[k].items():
                    where_placeholders = where_placeholders+f" {col}=%s AND "
                    values.append(val)
        arg_cols = "*"
        curr = self.db.cursor()
        place_holders = ""
        vals = ""
        query = f"SELECT {arg_cols} FROM {self.model_name}"+" WHERE"+place_holders 
        q_exec = curr.execute(query,vals)
        results = q_exec.fetchOne()
        self.db.close()
        return results
    
    def findAll(self,arg):
        pass
    # to delete
    def destroy(self,arg):
        pass
    
    def findAndUpdate(self,args):
        pass
    # used to create fields for the db, not used to create tables created thru migrations
    def init(self,model_name,args):
        if not isinstance(args,dict):
            # raise an error expecting a dict
            pass

        query = "create table query"
        self.model_name=model_name
        self.table_fields =args

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
    
    def __init__(self,dialect,db_config={},**kwargs):
        self.dialect = dialect
        self.db_config = db_config
        self.kwargs = kwargs
    def _unpack_kwargs(self):
        pass
    
    def connect(self):
        # call appropriate method based on provided dialect
        if self.dialect.lower() =="sqlite" or self.dialect.lower() =="sqlite3":
            self.sqlite_db()
        elif self.dialect.lower() =="mysql":
            self.mysql_db()
        pass
    def sqlite_db(self):
        import sqlite3
        # get db name from the kwargs

        conn = sqlite3.connect(self.kwargs)
        return conn
    
    def mysql_db(self):
        import mysql.connector as mysql_
        args= self.db_config
        db = mysql_.connect(
            host=args["host"],
            user=args["username"],
            password=args["password"],
            database=args["database"]
            )
        return db
    def postgress_db(self):
        pass
    def mssql_db(self):
        pass
    
    # other dbs


class Models_Migrate:
    pass

"""
------from test.py not here-------to be deleted----------
table={
    "username":{
        "type":"STRING",
        "allowNull":"False",
        "length":"12"
    },
    "password":{
        "type":"text",
    }
}
def col_func(args,col,attr):
    line = f"{col} "
    for key in args[col].keys():
        if key == "length":
            continue
        if key =="type":
            if "length" in args[col].keys():
                type_ = f"{args[col]['type']}({args[col]['length']})" 
                line = line +" "+ type_ +" "
            else:
                length = "15"
                type_ = f"{args[col]['type']}({length})" 
                line = line +" "+ type_ +" "
            continue
        if key.lower() == "allownull":
            if args[col][key]=="False":
                null = "NOT NULL"
                line = line +" "+ null
            continue
        line = line +" "+ key +" "
    return line
def unpack_table(args,t_name="users"):
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
#print(unpack_table(table))
ins={
    "username":"chaxes",
    "pana":"manlow",
    "user_id":"12"
}
def insert(args):
    len_args = len(args.keys())
    plcaholders= "("+"%,"*(len_args-1)+"%"+")"
    cols = "("
    for col in args.keys():
        cols =cols + col+","
    values = args.values()
    print(tuple(values))
    query = "INSERT INTO table_name" +cols[:-1] +")" +" VALUES"+ plcaholders
    print(query)
def select(args):
    where_placeholders = ""
    values = []
    cols ="*"
    
    for k,v in args.items():
        if k.lower() =="attributes":
            cols = ""
            cols = cols + " ,".join(args[k])
        if "attributes" not in args.keys():
            cols = "*"
        if k.lower() == "where":
            for col,val in args[k].items():
                where_placeholders = where_placeholders+f" {col}=%s AND "
                values.append(val)
    query = f"SELECT {cols} FROM table_name"+" WHERE "
    full_select = query +where_placeholders[:-4]
    print(full_select,tuple(values))
def update(args):
    pass
def delete(args):
    pass
selec ={
    "where":{
        "user":"panashe",
        "pass":"1234"
    },
    "attributes":["col1","col..."],
    "where2":{
        "Op.Or":{
            "col1":"val1..."
        }
    }
}
select(selec)
#insert(ins)
va = ["hello","manlow"]
val = "------>".join(va)
print(val)
"""