import SQLquery as sql
import queryType as qt

class QueryMaker:


    def  makeQuery (self, queryType, queryPayload):
              

        match queryType:
            case qt.QueryType.FINDPRODUCT :
                sqlQuery = sql.Query.findProduct
                
            case qt.QueryType.GETPRODUCTINFO :
                sqlQuery = sql.Query.readProduct
                

            case qt.QueryType.CREATEPRODUCT :
                sqlQuery = sql.Query.createProduct
                
                
            case qt.QueryType.DELETEPRODUCT :
                sqlQuery = sql.Query.deleteProduct
                
                
            case _:
                print("Error")
                return (None, None)
            
        return sqlQuery, queryPayload
    




testQuery = QueryMaker().makeQuery(qt.QueryType.CREATEPRODUCT, ("apple", 10))

print(testQuery)
    