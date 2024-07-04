import pyodbc as db
import pandas as pd
import regex as re

def getDtFrmFromDb(query):
    conn = None
    conn = db.connect('Driver={SQL Server};'
                    'Server=uvtsql.database.windows.net;'
                    'Database=db1;' #change to your own database
                    'uid=user32;' #change to your username
                    'pwd=CompEco1234;')
    dfObj  = pd.read_sql_query(query, conn)
    conn.close()
    return dfObj

##niet zelf bedacht
def getDomain(email):
    m = re.search('(?<=@).*', str(email).strip())
    if m:
        return m.group()

print(getDomain('hihi@hey.com'))
