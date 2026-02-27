from sql_requests import QueryProduct
from query_type import QueryType




"""
    Создаёт SQL-запрос на основе типа операции.

"""

class SQLqueryCreator:

    def __init__(self):
        self.sqlRequest = None

    def createSqlRequest(self, queryType: QueryType):


        match queryType:
            case QueryType.CREATEPRODUCT:
                self.sqlRequest = QueryProduct.CREATEPRODUCT

            case QueryType.GETPRODUCTINFO:
                self.sqlRequest = QueryProduct.GETPRODUCTINFO

            case QueryType.READPRODUCTLIST:
                self.sqlRequest = QueryProduct.READPRODUCTLIST

            case QueryType.FINDPRODUCT:
                self.sqlRequest = QueryProduct.FINDPRODUCT

            case QueryType.DELETEPRODUCT:
                self.sqlRequest = QueryProduct.DELETEPRODUCT



            case _:
                print ("Error")

        