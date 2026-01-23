import sqlite3
#import  modelProduct as mp
import query as qq


'''
class DBmanager:
    pass

'''        





def dataBaseAction(queryType):
    connection = sqlite3.connect("productsDB")

    dbAction = connection.cursor()

    dbQuery = qq.Query.createProduct
    



    match queryType:
        case "GET" :
            dbQuery = qq.Query.findProduct
            queryData = ("apple",)
        case "GET1" :
            dbQuery = qq.Query.readProduct
            queryData = (6,)

        case "POST" :
            dbQuery = qq.Query.createProduct
            queryData = ("apple", 10)
            
        case "DELETE" :
            dbQuery = qq.Query.deleteProduct
            queryData = (2,)
               
        case _:
            pass

    print(dbQuery)

    dbAction.execute(dbQuery, (queryData))
    queryResult = dbAction.fetchall()
    print(queryResult)




    connection.commit()
    connection.close()

    




dataBaseAction("POST")


