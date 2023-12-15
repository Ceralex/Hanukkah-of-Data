from db import create_cursor

def main():
    c = create_cursor("noahs.sqlite")
    """ 
    The text says that the woman arrived at 5am, so we assume she ordered a BKY(bakery) item between 4am and 5am.
    Then we group the customers by name and order them by the number of visits in descending order. Knowing she 
    is a regular customer, we can assume she is at the top of the list.
    """
    customers = c.execute("""
                            SELECT name, phone, COUNT(name) AS visits
                            FROM customers 
                            JOIN orders ON customers.customerid = orders.customerid
                            JOIN orders_items ON orders.orderid = orders_items.orderid
                            WHERE orders.ordered LIKE '% 04:%'
                            AND orders_items.sku LIKE 'BKY%'
                            GROUP BY customers.name
                            HAVING visits > 1
                            ORDER BY visits DESC
                          """).fetchall()
    for customer in customers:
        print(f"Name: {customer[0]} - Phone: {customer[1]} - Visits: {customer[2]}")

if __name__ == "__main__":
    main()