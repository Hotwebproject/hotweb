"""
used to define data types for different sql dialects

collect data types of different dialects and paste here

"""

DataTypes = {
    "mysql":{
        "STRING":"VARCHAR",
        "FLOAT":"FLOAT",
        "BIGINT":"BIGINT",
        "DATE":"DATE",
        "INTEGER":"INT"
    },# handle datatypes for mysql
    "pg":{

    },# for postgres
    "sqlite":{
        "STRING":"TEXT",
        "FLOAT":"REAL",
        "INTEGER":"INT",
        "BLOB":"BLOB"
    }# for sqlite
}