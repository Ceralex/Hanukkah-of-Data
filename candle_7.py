from db import create_cursor
 
def main():
    """ 
    We first searched for all the colored items that the 6th solution customer bought, then we
    joined the result with all the colored items that all the customers bought in the same date
    as hers, with the same product and a different color and bought within a time difference of 10 minutes or less.
    """
    c = create_cursor("noahs.sqlite")
    customers = c.execute('''
    SELECT * FROM (
    SELECT orders.shipped AS date, SUBSTR(
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
        SELECT orders.shipped AS date, customers.phone, customers.name, SUBSTR(
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
    AND ABS(JULIANDAY(Q1.date) - JULIANDAY(Q2.date)) * 1440 <= 10
''').fetchall()
   
    for customer in customers:
        print(customer)
   
 
if __name__ == "__main__":
    main()