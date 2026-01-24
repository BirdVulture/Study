from enum import Enum


class QueryType(Enum):
    FINDPRODUCT = "GET"
    GETPRODUCTINFO = "GET"
    CREATEPRODUCT = "POST"
    DELETEPRODUCT = "DELETE"
    READPRODUCTLIST = "GET"







