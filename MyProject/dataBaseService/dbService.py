import sqlite3
import queryType as qt
import queryManger as qm
 


'''
class DBmanager:
    pass

'''        





def dataBaseAction(queryType, queryPayload):
    connection = sqlite3.connect("productsDB")

    dbAction = connection.cursor()

    dbQuery, dbPayload = qm.QueryMaker().makeQuery(queryType, queryPayload)
    
  

    print(dbQuery)
    print(dbPayload)

    dbAction.execute(dbQuery, dbPayload) # type: ignore!!!!!
    queryResult = dbAction.fetchall()
    print(queryResult)




    connection.commit()
    connection.close()



# TEST
#dataBaseAction(qt.QueryType.CREATEPRODUCT, ("apple", 64))

#dataBaseAction(qt.QueryType.DELETEPRODUCT, (1,))




