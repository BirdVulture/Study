from query_creator import SQLqueryCreator
from query_type import QueryType




#TEST
query = QueryType.READPRODUCTLIST

test1 = SQLqueryCreator().createSqlRequest(query)

print(test1)