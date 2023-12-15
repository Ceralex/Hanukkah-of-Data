from db import create_cursor

def main():
    c = create_cursor("noahs.sqlite")
    neighborhood = c.execute("""
                             SELECT DISTINCT citystatezip FROM customers
                            JOIN orders ON orders.customerid = customers.customerid
                            JOIN orders_items ON orders.orderid = orders_items.orderid
                            WHERE shipped LIKE '2017-%'
                            AND customers.name LIKE 'J% P%'
                            AND orders_items.sku == (SELECT sku FROM products WHERE desc LIKE '%rug %')
                             """).fetchone()
    customer = c.execute(f"""
                            SELECT DISTINCT name, phone FROM customers
                            WHERE 
                                citystatezip = '{neighborhood[0]}' AND
                                ((birthdate BETWEEN '1939-06-21' AND '1939-07-23') OR
                                (birthdate BETWEEN '1951-06-21' AND '1951-07-23') OR
                                (birthdate BETWEEN '1975-06-21' AND '1975-07-23') OR
                                (birthdate BETWEEN '1987-06-21' AND '1987-07-23') OR
                                (birthdate BETWEEN '1999-06-21' AND '1999-07-23'))
                            
                          """
                          ).fetchone()
    print(customer)

if __name__ == "__main__":
    main()