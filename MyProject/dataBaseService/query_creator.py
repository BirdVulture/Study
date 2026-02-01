from sql_query import QueryProduct
from query_type import QueryType




"""
    Создаёт SQL-запрос на основе типа операции.

    Args:
        queryType (QueryType): Тип запроса.

    Returns:
        str | None: SQL-запрос или None, если тип не распознан.
"""
class SQLqueryCreator:

    def __init__(self):
        self.sqlRequest = None

    def createSqlRequest(self, queryType: QueryType):


        match queryType:
            case QueryType.CREATEPRODUCT:
                self.sqlRequest = QueryProduct.CREATEPRODUCT

            case QueryType.GETPRODUCTINFO:
                sqlRequest = QueryProduct.GETPRODUCTINFO

            case QueryType.READPRODUCTLIST:
                sqlRequest = QueryProduct.READPRODUCTLIST

            case QueryType.FINDPRODUCT:
                sqlRequest = QueryProduct.FINDPRODUCT

            case QueryType.DELETEPRODUCT:
                sqlRequest = QueryProduct.DELETEPRODUCT



            case _:
                print ("Error")

        return sqlRequest

#TEST

