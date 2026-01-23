class Query:
    createTable = 'CREATE TABLE IF NOT EXISTS products (' \
    'id INTEGER PRIMARY KEY,' \
    ' productName TEXT NOT NULL,' \
    ' productCalory INTEGER NOT NULL)'

    createProduct = 'INSERT INTO products (productName, productCalory) VALUES (?, ?)'
    findProduct = 'SELECT id FROM products WHERE productName = ?'
    readProduct = 'SELECT productName FROM products WHERE id = ?'
    deleteProduct = 'DELETE FROM products WHERE id = ?'



