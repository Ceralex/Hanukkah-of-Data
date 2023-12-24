from db import create_cursor
 
def main():
    c = create_cursor("noahs.sqlite")
    customers = c.execute('''
    SELECT * FROM (
    SELECT strftime('%Y %m %d', orders.shipped) AS date, SUBSTR(
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
    WHERE orders.customerid = 4167
    AND product IS NOT ''
    ) as Q1
    JOIN (
        SELECT strftime('%Y %m %d', orders.shipped) AS date, customers.phone, customers.name, SUBSTR(
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
        WHERE product IS NOT ''
    ) AS Q2 ON Q1.product = Q2.product
    AND Q1.color != Q2.color
    AND Q1.date = Q2.date
''').fetchall()
   
    for customer in customers:
        print(customer)
   
 
if __name__ == "__main__":
    main()