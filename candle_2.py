from db import create_cursor

def main():
    c = create_cursor("noahs.sqlite")
    customer = c.execute("""
                          SELECT DISTINCT name, phone, citystatezip FROM customers
                          JOIN orders ON orders.customerid = customers.customerid
                          JOIN orders_items ON orders.orderid = orders_items.orderid
                          WHERE shipped LIKE '2017-%'
                          AND customers.name LIKE 'J% P%'
                          AND orders_items.sku == (SELECT sku FROM products WHERE desc LIKE '%rug %')
                          """
                          ).fetchone()
    print(customer)

if __name__ == "__main__":
    main()