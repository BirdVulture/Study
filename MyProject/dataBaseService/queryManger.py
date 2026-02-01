import SQLquery as sql
import queryType as qt

class QueryMaker:


    def  makeQuery(self, queryType, queryPayload):
              

        match queryType:
            case qt.QueryType.READPRODUCTLIST:
                self.sqlQuery = sql.QueryProduct.READPRODUCTLIST

            case qt.QueryType.FINDPRODUCT :
                self.sqlQuery = sql.QueryProduct.FINDPRODUCT 
                
            #case qt.QueryType.GETPRODUCTINFO :
            #    self.sqlQuery =  
                
                
            #case qt.QueryType.CREATEPRODUCT :
            #    self.sqlQuery =  
                
                
            #case qt.QueryType.DELETEPRODUCT :
            #    self.sqlQuery = 

            case _:
                print("Error")
                return (None, None)
            
        return self.sqlQuery, queryPayload
    



#TEST

testQuery = QueryMaker().makeQuery(qt.QueryType.READPRODUCTLIST, (10,))
testQuery1 = QueryMaker().makeQuery(qt.QueryType.FINDPRODUCT, (10,))
#testQuery2 = QueryMaker().makeQuery(qt.QueryType.GETPRODUCTINFO, (10,))
#testQuery3 = QueryMaker().makeQuery(qt.QueryType.CREATEPRODUCT, ("apple", 10))
#testQuery4 = QueryMaker().makeQuery(qt.QueryType.DELETEPRODUCT, (10,))

print(testQuery)
print(testQuery1)
     