class QueryProduct:
    #CREATETABLE = 'CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, productName TEXT NOT NULL, productCalory INTEGER NOT NULL)'
    
    CREATEPRODUCT = 'INSERT INTO products (productName, productCalory) VALUES (?, ?)'

    FINDPRODUCT = 'SELECT id FROM products WHERE productName = ?'
    
    READPRODUCTINFO = 'SELECT productName, productCalory FROM products WHERE id = ?'
    
    DELETEPRODUCT = 'DELETE FROM products WHERE id = ?'

    READPRODUCTLIST = 'SELECT * FROM products LIMIT ?'



#TEST
"""
testSQLquery = QueryProduct().CREATEPRODUCT
print(testSQLquery)

testSQLquery1 = QueryProduct().FINDPRODUCT
print(testSQLquery1)


testSQLquery2 = QueryProduct().READPRODUCTINFO
print(testSQLquery2)

testSQLquery3 = QueryProduct().DELETEPRODUCT
print(testSQLquery3)

testSQLquery4 = QueryProduct().READPRODUCTLIST
print(testSQLquery4)

"""













