import sqlite3
#import  modelProduct as mp
import query as qq


'''
class DBmanager:
    pass

'''        





def dataBaseAction():
    connection = sqlite3.connect("productsDB")

    dbAction = connection.cursor()

    dbQuery = qq.Query.createProduct


    print(dbQuery)

    dbAction.execute(dbQuery, ('apple', 3))

    connection.commit()
    connection.close()
    



dataBaseAction()


