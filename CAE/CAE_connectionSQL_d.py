import pyodbc as db
import pandas as pd
import regex as re
from CAE_connectionSQL_c import getDtFrmFromDb
from CAE_connectionSQL_c import getDomain

##niet zelf bedacht
def getListFromDb(query):
    conn = None
    conn = db.connect('Driver={SQL Server};'
                    'Server=uvtsql.database.windows.net;'
                    'Database=db1;' #change to your own database
                    'uid=user32;' #change to your username
                    'pwd=CompEco1234;')

    # #read into list
    cursor = conn.cursor()
    cursor.execute(query)

    lsObj = list(cursor.fetchall())
    list_of_lists = [list(elem) for elem in lsObj]

    cursor.close()
    conn.close()

    return list_of_lists

print(getListFromDb('select * from Customers'))

def makeLower(npl_biblio):
    npl_biblio_low = npl_biblio.lower()
    return npl_biblio_low

def main():
    sql_query = 'select * from Customers'
    dfObj = getDtFrmFromDb(sql_query)
    print(dfObj)

    input("press Enter to continue......")
    cursor_list = getListFromDb(sql_query)

    for i in range(len(cursor_list)):
        print(cursor_list[i][8])

    input("press Enter to continue......")
    print("----------------------------------------------------------------------------------------------")

    for k in range(len(cursor_list)):
        print("cust_id: ", cursor_list[k][0])
        t = cursor_list[k][8]
        print("email: ", t)
        print("domain ", getDomain(t))
        print()

    input("press Enter to continue...")

    dfObj['EmailDomain'] = dfObj['cust_email'].apply(getDomain)
    print(dfObj[['EmailDomain']])

main()
