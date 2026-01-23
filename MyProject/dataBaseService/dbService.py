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
    dbQuery1 = qq.Query.deleteProduct



    match queryType:
        case "GET" :
            pass
        case "POST" :
            pass
        case "DELETE" :
            pass        
        case _:
            pass

    print(dbQuery)

    #dbAction.execute(dbQuery, ('bread', 4))

    #dbAction.execute(dbQuery1, (2,)) 

    connection.commit()
    connection.close()
    



dataBaseAction()


