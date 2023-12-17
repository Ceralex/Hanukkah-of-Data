from db import create_cursor
 
def main():
    c = create_cursor("noahs.sqlite")
    customers = c.execute("""
                            SELECT customers.name, customers.phone, COUNT(orders.customerid) AS n_risparmi FROM (
                                SELECT orders.customerid, orders.total AS paid, SUM(products.wholesale_cost * orders_items.qty) AS price FROM orders
                                JOIN orders_items ON orders.orderid = orders_items.orderid
                                JOIN products ON orders_items.sku = products.sku
                                GROUP BY orders.orderid
                            ) AS orders
                            JOIN customers ON orders.customerid = customers.customerid
                            WHERE paid < price
                            GROUP BY orders.customerid
                            ORDER BY n_risparmi DESC
                            LIMIT 3
                          """).fetchall()
    for customer in customers:
        print(f"Name: {customer[0]} - Phone: {customer[1]} - Coupon used: {customer[2]}")
   
 
if __name__ == "__main__":
    main()