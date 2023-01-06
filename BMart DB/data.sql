USE kjhk;

INSERT INTO store(country, region, address, zip_code, phone_number) VALUES("USA", "Illinois", "100 E Chicago Street", 60007, "832-412-6432");
INSERT INTO store(country, region, address, zip_code, phone_number) VALUES("USA", "Illinois", "600 S Springfield Street", 62629, "212-456-0934");
INSERT INTO store(country, region, address, zip_code, phone_number) VALUES("USA", "California", "200 E Pasadena Street", 91001, "551-398-4028");
INSERT INTO store(country, region, address, zip_code, phone_number) VALUES("CAN", "SnowLand", "100 W Snow Street", 42042, "572-829-2759");
INSERT INTO store(country, region, address, zip_code, phone_number) VALUES("FRA", "BaguetteLand", "1530 N White Flag Street", 75003, "389-475-1000");
INSERT INTO store(country, region, address, zip_code, phone_number) VALUES("USA", "Texas", "620 N Brisket Street", 77002, "654-203-9677");

INSERT INTO vendor VALUES(1, "Fox Incorporated");
INSERT INTO vendor VALUES(2, "Penguin Incorporated");

INSERT INTO brands VALUES("Arctic Fox Electronics", 1);
INSERT INTO brands VALUES("Galactic Penguin Food", 2);
INSERT INTO brands VALUES("Penguin Town", 2);
INSERT INTO brands VALUES("Foxy Fancy FunWear", 1);

INSERT INTO product VALUES(111000, "Time Machine", "Arctic Fox Electronics", 10, "USA", 100, "item");
INSERT INTO product VALUES(222000, "Shrink Ray", "Arctic Fox Electronics", 20, "USA", 200, "item");
INSERT INTO product VALUES(333000, "Teleporter", "Arctic Fox Electronics", 30, "USA", 300, "item");
INSERT INTO product VALUES(444000, "Penguin Pellets", "Galactic Penguin Food", 40, "CAN", 400, "pound");
INSERT INTO product VALUES(555000, "Gentoo Tofu", "Galactic Penguin Food", 50, "CAN", 500, "pound");
INSERT INTO product VALUES(666000, "FlipFlap Sardines", "Galactic Penguin Food", 60, "CAN", 500, "pound");
INSERT INTO product VALUES(777000, "Emporer Penguin", "Penguin Town", 70, "USA", 700, "animal");
INSERT INTO product VALUES(888000, "Southern Rockhopper Penguin", "Penguin Town", 80, "USA", 800, "animal");
INSERT INTO product VALUES(999000, "King Penguin", "Penguin Town", 90, "FRA", 900, "animal");
INSERT INTO product VALUES(101000, "Fox Fur Suspenders", "Foxy Fancy FunWear", 100, "FRA", 1000, "item");
INSERT INTO product VALUES(111100, "Fox Fur Bandana", "Foxy Fancy FunWear", 110, "FRA", 1100, "item");
INSERT INTO product VALUES(121200, "Fox Fur Sunglasses", "Foxy Fancy FunWear", 120, "CAN", 1200, "item");

INSERT INTO product_types VALUES(111000, "Device");
INSERT INTO product_types VALUES(222000, "Gun");
INSERT INTO product_types VALUES(333000, "Teleporter");
INSERT INTO product_types VALUES(444000, "Pellets");
INSERT INTO product_types VALUES(555000, "Tofu");
INSERT INTO product_types VALUES(666000, "Sardines");
INSERT INTO product_types VALUES(777000, "Emperor Joe");
INSERT INTO product_types VALUES(888000, "Southern Bob");
INSERT INTO product_types VALUES(999000, "King Scott");
INSERT INTO product_types VALUES(101000, "Suspenders");
INSERT INTO product_types VALUES(111100, "Bandana");
INSERT INTO product_types VALUES(121200, "Sunglasses");

INSERT INTO inventory(upc, store_id, item_count, capacity, store_price) VALUES(111000, 1, 60, 60, 40.99);
INSERT INTO inventory(upc, store_id, item_count, capacity, store_price) VALUES(222000, 1, 75, 75, 82.99);
INSERT INTO inventory(upc, store_id, item_count, capacity, store_price) VALUES(333000, 1, 45, 80, 37.99);
INSERT INTO inventory(upc, store_id, item_count, capacity, store_price) VALUES(444000, 2, 55, 105, 120.99);
INSERT INTO inventory(upc, store_id, item_count, capacity, store_price) VALUES(555000, 2, 125, 160, 260.99);
INSERT INTO inventory(upc, store_id, item_count, capacity, store_price) VALUES(666000, 4, 478, 500, 41.99);
INSERT INTO inventory(upc, store_id, item_count, capacity, store_price) VALUES(777000, 4, 96, 160, 4200.99);
INSERT INTO inventory(upc, store_id, item_count, capacity, store_price) VALUES(888000, 3, 19, 20, 1256.99);
INSERT INTO inventory(upc, store_id, item_count, capacity, store_price) VALUES(999000, 3, 2, 5, 1663.99);
INSERT INTO inventory(upc, store_id, item_count, capacity, store_price) VALUES(101000, 5, 102, 175, 140.99);
INSERT INTO inventory(upc, store_id, item_count, capacity, store_price) VALUES(111100, 5, 31, 50, 10.99);
INSERT INTO inventory(upc, store_id, item_count, capacity, store_price) VALUES(121200, 5, 79, 100, 4.99);
  
INSERT INTO customers(c_name, c_email, c_phone) VALUES("Steve Rogers", "thecap1920@avengers.com", "111-222-3333");
INSERT INTO customers(c_name, c_email, c_phone) VALUES("Tony Stark", "IamIronman@avengers.com", "444-555-6666");
INSERT INTO customers(c_name, c_email, c_phone) VALUES("Thor Odinson", "GodOfThunder@avengers.com", "777-888-9999");
INSERT INTO customers(c_name, c_email, c_phone) VALUES("Natasha Romanoff", "Call-Me-Soulstone@avengers.com", "012-345-6789");

INSERT INTO hours(store_id, weekday, open_at, close_at) VALUES(1, "Mon", "07:00", "20:00");
INSERT INTO hours(store_id, weekday, open_at, close_at) VALUES(1, "Tue", "07:00", "20:00");
INSERT INTO hours(store_id, weekday, open_at, close_at) VALUES(1, "Wed", "07:00", "20:00");
INSERT INTO hours(store_id, weekday, open_at, close_at) VALUES(1, "Thu", "07:00", "20:00");
INSERT INTO hours(store_id, weekday, open_at, close_at) VALUES(1, "Fri", "07:00", "20:00");
INSERT INTO hours(store_id, weekday, closed) VALUES(1, "Sat", 1);
INSERT INTO hours(store_id, weekday, closed) VALUES(1, "Sun", 1);

INSERT INTO hours(store_id, weekday, open_at, close_at) VALUES(2, "Mon", "06:00", "17:00");
INSERT INTO hours(store_id, weekday, open_at, close_at) VALUES(2, "Tue", "06:00", "17:00");
INSERT INTO hours(store_id, weekday, open_at, close_at) VALUES(2, "Wed", "06:00", "17:00");
INSERT INTO hours(store_id, weekday, open_at, close_at) VALUES(2, "Thu", "06:00", "17:00");
INSERT INTO hours(store_id, weekday, open_at, close_at) VALUES(2, "Fri", "06:00", "17:00");
INSERT INTO hours(store_id, weekday, closed) VALUES(2, "Sat", 1);
INSERT INTO hours(store_id, weekday, closed) VALUES(2, "Sun", 1);

INSERT INTO online_order(order_status, customer_id, store_id) VALUES ("Shipped", 1, 1);
INSERT INTO online_order(order_status, customer_id, store_id) VALUES ("Fulfilled", 2, 2);
INSERT INTO online_order(order_status, customer_id, store_id) VALUES ("Arrived", 3, 3);
INSERT INTO online_order(order_status, customer_id, store_id) VALUES ("Delayed", 4, 4);

INSERT INTO online_order_items(online_order_id, upc, order_qty, purchase_price) VALUES (1, 111000, 20, 2000.00);
INSERT INTO online_order_items(online_order_id, upc, order_qty, purchase_price) VALUES (1, 222000, 30, 6000.00);
INSERT INTO online_order_items(online_order_id, upc, order_qty, purchase_price) VALUES (1, 333000, 40, 12000.00);
INSERT INTO online_order_items(online_order_id, upc, order_qty, purchase_price) VALUES (2, 666000, 20, 7000.00);
INSERT INTO online_order_items(online_order_id, upc, order_qty, purchase_price) VALUES (2, 444000, 50, 20000.00);
INSERT INTO online_order_items(online_order_id, upc, order_qty, purchase_price) VALUES (3, 777000, 20, 42000.00);
INSERT INTO online_order_items(online_order_id, upc, order_qty, purchase_price) VALUES (3, 444000, 40, 22000.00);
INSERT INTO online_order_items(online_order_id, upc, order_qty, purchase_price) VALUES (3, 999000, 40, 12000.00);
INSERT INTO online_order_items(online_order_id, upc, order_qty, purchase_price) VALUES (4, 888000, 20, 1200.00);

INSERT INTO local_order(customer_id, store_id) VALUES(1, 5);
INSERT INTO local_order(customer_id, store_id) VALUES(2, 6);
INSERT INTO local_order(customer_id, store_id) VALUES(3, 1);
INSERT INTO local_order(customer_id, store_id) VALUES(4, 2);

INSERT INTO local_order_items(local_order_id, upc, order_qty, purchase_price) VALUES(1, 111000, 2, 82.00);
INSERT INTO local_order_items(local_order_id, upc, order_qty, purchase_price) VALUES(1, 222000, 7, 122.00);
INSERT INTO local_order_items(local_order_id, upc, order_qty, purchase_price) VALUES(1, 333000, 11, 162.00);
INSERT INTO local_order_items(local_order_id, upc, order_qty, purchase_price) VALUES(2, 444000, 24, 632.00);
INSERT INTO local_order_items(local_order_id, upc, order_qty, purchase_price) VALUES(2, 555000, 70, 6242.00);
INSERT INTO local_order_items(local_order_id, upc, order_qty, purchase_price) VALUES(2, 666000, 41, 18432.00);
INSERT INTO local_order_items(local_order_id, upc, order_qty, purchase_price) VALUES(3, 777000, 23, 8222.00);
INSERT INTO local_order_items(local_order_id, upc, order_qty, purchase_price) VALUES(3, 888000, 55, 6531.00);
INSERT INTO local_order_items(local_order_id, upc, order_qty, purchase_price) VALUES(1, 999000, 2, 176.00);
