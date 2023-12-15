from db import create_cursor

def main():
    c = create_cursor("noahs.sqlite")
    """
    In the text they say the woman has a sweatshirt, but the right woman has only bought a jewelry item, not a sweatshirt/jersey. 
    So probably the database entry was wrong.
    Anyway, we select all the customers that bought more than 10 times cat items (she says she has 10 cats) and at least one jewelry item.
    """
    customers = c.execute("""
                            SELECT name, phone, COUNT(customers.name) AS n_orders FROM customers
                            JOIN orders ON customers.customerid = orders.customerid
                            JOIN orders_items ON orders.orderid = orders_items.orderid
                            JOIN products ON orders_items.sku = products.sku
                            WHERE products.desc LIKE '%cat%'
                            AND customers.citystatezip LIKE 'Staten Island, NY %'
                            AND customers.name IN (
                                SELECT name FROM customers
                                JOIN orders ON customers.customerid = orders.customerid
                                JOIN orders_items ON orders.orderid = orders_items.orderid
                                JOIN products ON orders_items.sku = products.sku
                                WHERE products.desc LIKE '%jewelry%'
                            )
                            GROUP BY customers.name
                            HAVING n_orders > 10
                            ORDER BY n_orders DESC
                          """).fetchall()
    
    for customer in customers:
        print(f"Name: {customer[0]} - Phone: {customer[1]} - Orders: {customer[2]}")

    

if __name__ == "__main__":
    main()