import sqlite3
import queryType as qt
import queryManger as qm
 
class DBAction:

    def __init__(self):
        self.queryResult = None

    def __del__(self):
        pass
    
    def doQuery(self, queryType, queryPayload):
        connection = sqlite3.connect("productsDB")

        dbAction = connection.cursor()

        dbQuery, dbPayload = qm.QueryMaker().makeQuery(queryType, queryPayload)
        
    

        print(dbQuery)
        print(dbPayload)

        #нужно добавить try
        #нужно добавить обработку результата в зависимости от запроса

        dbAction.execute(dbQuery, dbPayload) # type: ignore
        
        #dbAction.execute('SELECT * FROM products LIMIT ?', (5,)) # Для тестирования SQL запросов
        
        self.queryResult = dbAction.fetchall()
        
        print(self.queryResult)




        connection.commit()
        connection.close()



# TEST
testObject = DBAction()

testObject.doQuery(qt.QueryType.READPRODUCTLIST, (10,))
print(testObject.queryResult)

print(testObject)
testObject.__del__()
print(testObject)


#dataBaseAction(qt.QueryType.CREATEPRODUCT, ("apple", 64))

#dataBaseAction(qt.QueryType.DELETEPRODUCT, (1,))

#dataBaseAction(qt.QueryType.READPRODUCTLIST, (5,))

