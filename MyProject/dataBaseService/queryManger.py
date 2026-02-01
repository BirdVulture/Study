from SQLquery import QueryProduct
from queryType import QueryType


def sqlQueryCreator(queryType):
    
    sqlRequest = None

    match queryType:
        case QueryType.FINDPRODUCT:
            sqlRequest = QueryProduct.FINDPRODUCT

        case QueryType.GETPRODUCTINFO:
            sqlRequest = QueryProduct.READPRODUCTINFO

        case _:
            print ("Error")

    return sqlRequest

#TEST

test1 = sqlQueryCreator(QueryType.FINDPRODUCT)
test2 = sqlQueryCreator(QueryType.GETPRODUCTINFO)


print(test1)
print(test2)
