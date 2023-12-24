from db import create_cursor

def main():
    c = create_cursor("noahs.sqlite")
    customers = c.execute('''
    SELECT COUNT(desc) as collection, customers.name, customers.phone, SUBSTR(
            desc,
            0,
            INSTR(desc, '(') - 1
        ) AS product,
        SUBSTR(
            desc,
            INSTR(desc, '(') + 1,
            INSTR(desc, ')') - INSTR(desc, '(') - 1
        ) AS color FROM orders
    JOIN orders_items ON orders.orderid = orders_items.orderid
    JOIN products ON orders_items.sku = products.sku
    JOIN customers ON orders.customerid = customers.customerid
    WHERE color != ''
    AND products.sku LIKE 'COL%'
    GROUP BY customers.customerid
    ORDER BY collection DESC
    LIMIT 3
''').fetchall()
    for customer in customers:
        print(customer)
    

if __name__ == "__main__":
    main()