import sqlite3
import queryType as qt
import queryManger as qm
import queryStatus as qs
 

#нужно добавить try ГОТОВО
#нужно добавить обработку результата в зависимости от запроса ГОТОВО
#Нужно добавить тесты для всех методов




class DBQuery:

    def __init__(self):
        self.queryResult = {
            "queryStatus": None,
            "queryAnswer": None
            }

        
    def doQuery(self, queryType, queryPayload):
        connection = sqlite3.connect("productsDB")

        dbAction = connection.cursor()

        dbQuery, dbPayload = qm.QueryMaker().makeQuery(queryType, queryPayload)
        

        
        try:

            dbAction.execute(dbQuery, dbPayload) # type: ignore
            self.queryResult["queryStatus"] = qs.QueryStatus.OK # type: ignore

            match queryType:
                case qt.QueryType.READPRODUCTLIST:
                    self.queryResult["queryAnswer"] = dbAction.fetchall() # type: ignore

                case qt.QueryType.GETPRODUCTINFO :
                    self.queryResult["queryAnswer"] = dbAction.fetchall() # type: ignore

                case _:
                    pass
                   
            #dbAction.execute('SELECT * FROM products LIMIT ?', (5,)) # Для тестирования SQL запросов

        except:
            self.queryResult["queryStatus"] = qs.QueryStatus.ERROR # type: ignore

        
        print(f"\nПроверка 1 {self.queryResult}")




        connection.commit()
        connection.close()



# TEST
testObject = DBQuery()

#testObject.doQuery(qt.QueryType.READPRODUCTLIST, (10,))
#testObject.doQuery(qt.QueryType.GETPRODUCTINFO, (10,))
testObject.doQuery(qt.QueryType.FINDPRODUCT, (10,))


print(f"\nПроверка 2{testObject.queryResult["queryAnswer"]}")


print(testObject)


#dataBaseAction(qt.QueryType.CREATEPRODUCT, ("apple", 64))

#dataBaseAction(qt.QueryType.DELETEPRODUCT, (1,))

#dataBaseAction(qt.QueryType.READPRODUCTLIST, (5,))

#1596

