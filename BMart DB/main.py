import mysql.connector
from datetime import datetime
from mysql.connector import errorcode


# DB connection function
def db_connect():
    try:
        cnx = mysql.connector.connect(user='KJHK', password='databasepanic', host='cs314.iwu.edu', database='kjhk')
        return cnx

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


# Josh's Function
def shipment(store: int, delivery_date: datetime, reorders: list, shipment_items: dict):
    """Takes as input the store id as an int, the delivery date as a datetime object, the reorders being fulfilled as a list of the reorder ids, and a dictionary containing item upcs as keys and the quantities as their respective values."""

    cnx = db_connect()
    if cnx:  # If the connection failed, cnx will be a None and the function will close safely

        try:
            cursor = cnx.cursor()

            for order in reorders:
                query = 'SELECT fulfillment_status FROM store_order_items WHERE reorder_id = %s'
                params = (order,)
                cursor.execute(query, params)

                row = cursor.fetchone()
                if row[0] == 1:
                    print('Reorder ' + str(order) + ' has already been fulfilled! Remove it and try again.')
                    return

            query = 'INSERT INTO incoming_shipments (expected_arrival_date) VALUES (%s)'
            params = (delivery_date,)
            cursor.execute(query, params)

            cursor.execute('SELECT LAST_INSERT_ID()')  # Retrieving the autoincrementing shipment id
            shipment_id = cursor.fetchone()[0]

            for item in shipment_items:
                try:
                    query = 'INSERT INTO shipment_items VALUES (%s, %s, %s)'
                    params = (shipment_id, item, shipment_items[item])
                    cursor.execute(query, params)
                except mysql.connector.Error as err:
                    print("Invalid shipment item " + str(item) + "!")
                    print(str(err))
                    cnx.rollback()

            for order in reorders:
                try:
                    query = 'UPDATE store_order_items SET fulfillment_status = 1 WHERE reorder_id = %s'
                    params = (order,)
                    cursor.execute(query, params)

                except mysql.connector.Error as err:
                    print("Error updating fulfillment status of reorder for " + str(order) + "!")
                    print(str(err))
                    cnx.rollback()

            cnx.commit()

            print('Shipment Manifest:')
            for item in shipment_items:
                print('Item:', item, 'Quantity', shipment_items[item])
            print('Orders fulfilled:')
            for order in reorders:
                print(order)

            try:
                query = 'SELECT COUNT(*) FROM store_order_items WHERE store_id = %s AND fulfillment_status = 0'
                params = (store,)
                cursor.execute(query, params)

                row = cursor.fetchone()

                if row is None:
                    row = 0

                print('There are ' + str(row[0]) + ' remaining unfulfilled orders from BMart store ' + str(store))
            except mysql.connector.Error as err:
                print('Error finding unfulfilled store orders!')
                print(str(err))

            try:
                cursor.execute('SELECT COUNT(*) FROM store_order_items WHERE fulfillment_status = 0')
                row = cursor.fetchone()

                if row is None:
                    row = 0

                print('There are ' + str(row[0]) + ' remaining unfulfilled orders from all BMart stores')
            except mysql.connector.Error as err:
                print('Error finding unfulfilled orders from all BMart stores!')
                print(str(err))

        except mysql.connector.Error as err:
            print('Error while executing', cursor.statement, '--', str(err))
            cnx.rollback()

        finally:
            cnx.close()


# Khumoyun's Function
def online_order(store: int, customer: int, order_items: dict):
    """Takes as input the store id as an int, the customer id as an int, and the items being ordered as a dictionary with upcs as keys and quantaties as values """
    cnx = db_connect()
    if cnx:  # If the connection failed, cnx will be a None and the function will close safely

        try:
            cursor = cnx.cursor()

            # verify the customer and store their information for later
            query = "SELECT c_email, c_name FROM customers WHERE customer_id = %s"
            params = (customer,)
            cursor.execute(query, params)
            row = cursor.fetchone()

            if not row:
                print("Invalid customer id! Make sure you sign up before placing any orders")
                return

            user_info = [row[0], row[1]]  # Email and name respectively

            # create an order
            query = 'INSERT INTO online_order (order_status, customer_id, store_id) VALUES (%s, %s, %s)'
            params = ("PROCESSING", customer, store)
            cursor.execute(query, params)

            cursor.execute('SELECT LAST_INSERT_ID()')  # Retrieving the autoincrementing shipment id
            order_id = cursor.fetchone()[0]

            items = {}
            total = 0

            # add each item to order_items and connect to the order
            for item in order_items:

                try:
                    # Check inventory for item

                    query = 'SELECT item_count FROM inventory WHERE store_id = %s AND upc = %s'
                    params = (store, item)
                    cursor.execute(query, params)

                    quantity = cursor.fetchone()

                    if not quantity or quantity[0] < order_items[item]:
                        print('Store ' + str(store) + ' has insufficient stock for item ' + str(item) + '!')

                        # Attempt to find other stores with the item
                        try:
                            query = 'SELECT s.store_id FROM store AS s JOIN inventory AS i ON s.store_id = i.store_id ' \
                                    'WHERE i.upc = %s AND i.item_count >= %s AND ' \
                                    's.region = (SELECT region FROM store WHERE store_id = %s)'
                            params = (item, order_items[item], store)
                            cursor.execute(query, params)

                            alt_stores = []

                            for row in cursor:
                                alt_stores.append(row[0])

                            if len(alt_stores) == 0:
                                print('No other stores in this region have sufficient stock for item ' + str(item))
                                return

                            print('The following stores in this region have sufficient stock for item ' + item + ':')
                            for store in alt_stores:
                                print(store)

                            return

                        except mysql.connector.Error as err:
                            print('Error finding alternate stores', str(err))
                            return

                    query = 'INSERT INTO online_order_items (online_order_id, upc, order_qty) VALUES (%s, %s, %s)'
                    params = (order_id, item, order_items[item])
                    cursor.execute(query, params)

                    # update inventory
                    update = "UPDATE inventory SET item_count = item_count - %s WHERE store_id = %s AND upc = %s"
                    params = (order_items[item], store, item)
                    cursor.execute(update, params)

                    # keep track of the total
                    query = 'SELECT store_price FROM inventory WHERE upc = %s'
                    params = (item,)
                    cursor.execute(query, params)
                    price = cursor.fetchone()[0]
                    total += price * order_items[item]

                    # get names of the items from the db to print out to the user at the end
                    query = 'SELECT product_name FROM product WHERE upc = %s'
                    params = (item,)
                    cursor.execute(query, params)
                    product_name = cursor.fetchone()[0]
                    items[product_name] = order_items.get(item)

                except mysql.connector.Error as err:
                    print("Invalid order item " + str(item) + "!", str(err), cursor.statement)
                    cnx.rollback()

            # Customer output
            print(
                f"Order has been placed successfully. Details: \nName: {user_info[1]} \nEmail: {user_info[0]} \nCustomer ID: {customer}. ")
            print("Items:")
            for item in items:
                print(item, "(" + str(items[item]) + ")")

            cnx.commit()

        except mysql.connector.Error as err:
            print('Error while executing', cursor.statement, '--', str(err))
            cnx.rollback()
        finally:
            cnx.close()


# Hector's Function
def reorder(store_id: int):
    """
      -Function that checks specificed store for inventory that
      needs reordering and reorder product is so.
      -Prints a list of active orders at end of function.

      {param} store_id -> numeric value identifier unique to Bmart store.
      {return} none
    """

    cnx = db_connect()
    if cnx:
        try:
            cursor = cnx.cursor(buffered=True)  # Due to iterating below, needed to avoid unread result errors

            query = 'SELECT upc, item_count, capacity, store_price, is_ordered FROM inventory WHERE store_id = %s'
            params = (store_id,)
            cursor.execute(query, params)  # getting inventory for specified store

            reorder_total = 0  # total amount reorder will cost local store

            for row in cursor:  # every item (upc) in inventory

                upc = row[0]
                item_count = row[1]
                capacity = row[2]
                store_price = row[3]
                order_status = row[4]

                if item_count < capacity:  # if count is less than capacity
                    if order_status == 0:  # ensure duplicate reoder does not occur where 0 == False, 1 == True
                        order_qty = capacity - item_count  # Calculating how much to reorder
                        price = store_price * order_qty  # Calculating price of items that need to be reordered
                        reorder_total = reorder_total + price  # adding price of ordered product to total

                        internal_cursor = cnx.cursor()

                        query = 'INSERT INTO store_order_items (store_id, upc, order_qty, cost) VALUES (%s, %s, %s, %s)'
                        params = (store_id, upc, order_qty, float(price))
                        internal_cursor.execute(query, params)  # adding order item to store orders table

                        query = 'UPDATE inventory SET is_ordered = %s WHERE store_id = %s'
                        params = (1, store_id)
                        internal_cursor.execute(query, params)  # updating inventory order status to 1

                        print("Item " + str(row[0]) + " has been successfully ordered for store " + str(store_id) + '.')
                    else:
                        print("Item " + str(row[0]) + " is already on order for store " + str(store_id) + '.')

            print("\nTotal Price: $" + str(float(reorder_total)))
            print("-" * 50)

            cnx.commit()

        except mysql.connector.Error as err:
            print('Execution Error: Could Not Complete Orders', cursor.statement, '--', str(err))
            cnx.rollback()

        finally:
            cnx.close()


# Karthi's Function
def stock(store: int, shipment: int, shipment_items: dict):
    """Takes as input the store id as an int, the shipment id as an int, and the shipment items as a dictionary containing the upcs (keys) and the quantity actually received (values)"""

    cnx = db_connect()

    if cnx:
        try:
            cur = cnx.cursor()

            try:
                # Record shipment arrival time
                query = "UPDATE incoming_shipments SET actual_arrival_date = %s WHERE shipment_id = %s"
                parameters = (datetime.now(), shipment)
                cur.execute(query, parameters)
            except mysql.connector.Error as err:
                print('Error updating shipment arrival time!', str(err))

            for item in shipment_items:

                # Gets number of items and its maximum capacity to check to make sure total items can't exceed capacity
                query = "SELECT item_count, capacity FROM inventory JOIN store ON store.store_id = %s WHERE upc = %s"
                parameters = (store, item)
                cur.execute(query, parameters)
                result = cur.fetchone()

                number_of_items = result[0]
                capacity = result[1]

                total = number_of_items + shipment_items[item]

                # If new total is not exceeding max capacity, change the number of items to new total
                if total <= capacity:
                    try:
                        query = "UPDATE inventory SET item_count = %s, is_ordered = 0 WHERE store_id = %s AND upc = %s"
                        parameters = (total, store, item)
                        cur.execute(query, parameters)
                    except mysql.connector.Error as err:
                        print('Error updating inventory for item', item, cur.statement, '--',
                              str(err))
                        cnx.rollback()
                else:
                    print('Product ', item, ' has exceeded maximum capacity')
                    cnx.rollback()
                    return

            disc_track = [{}, {}]  # Discrepancy tracking

            try:
                query = 'SELECT upc, quantity FROM shipment_items WHERE shipment_id = %s'
                parameters = (shipment,)
                cur.execute(query, parameters)

                print('Shipment as described by vendor:')
                for row in cur:
                    print(row[0], row[1])
                    disc_track[0][row[0]] = row[1]
            except mysql.connector.Error as err:
                print('Error retrieving shipment as described by vendor', str(err))

            print('Shipment received:')
            for item in shipment_items:
                print(item, shipment_items[item])
                disc_track[1][item] = shipment_items[item]

            discrepancies = []

            for item in disc_track[0]:
                try:
                    if disc_track[0][item] != disc_track[1][item]:
                        discrepancies.append(
                            'Expected: ' + str(disc_track[0][item]) + ' of ' + str(item) + '; Received: ' + str(
                                disc_track[1][item]))
                except KeyError:
                    discrepancies.append(
                        'Expected: ' + str(disc_track[0][item]) + ' of ' + str(item) + '; Received NONE')

            for disc in discrepancies:
                print(disc)

            if len(discrepancies) == 0:
                print('No discrepancies found')

            cnx.commit()

        except mysql.connector.Error as err:
            print('Failed to stock inventory.', cur.statement, '--', str(err))
            cnx.rollback()
        finally:
            cnx.close()

