USE kjhk;

DROP TABLE IF EXISTS local_order_items;
DROP TABLE IF EXISTS local_order;
DROP TABLE IF EXISTS online_order_items;
DROP TABLE IF EXISTS online_order;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS shipment_items;
DROP TABLE IF EXISTS incoming_shipments;
DROP TABLE IF EXISTS store_order_items;
DROP TABLE IF EXISTS hours;
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS product_types;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS brands;
DROP TABLE IF EXISTS vendor;

CREATE TABLE vendor (
  vendor_id int,
  vendor_name varchar(30),
  PRIMARY KEY (vendor_id)
);

CREATE TABLE brands (
  brand_name varchar(30),
  vendor_id int,
  PRIMARY KEY (brand_name),
  FOREIGN KEY (vendor_id) REFERENCES vendor(vendor_id)
);

CREATE TABLE product (
  upc int,
  product_name varchar(30),
  brand_name varchar(30),
  weight int,
  source_nation char(3), -- Country codes
  standard_price decimal(9,2) NOT NULL, 
  unit varchar(30) NOT NULL, 
  PRIMARY KEY (upc),
  FOREIGN KEY (brand_name) REFERENCES brands(brand_name)
);

CREATE TABLE product_types (
  upc int,
  type varchar(15),
  PRIMARY KEY (upc, type),
  FOREIGN KEY (upc) REFERENCES product(upc)
);

CREATE TABLE inventory (
  upc int, 
  store_id int,
  item_count int NOT NULL, 
  capacity int NOT NULL,  
  store_price decimal(9,2), -- Max for 5 bytes; plenty of storage 
  is_ordered bit DEFAULT 0, 
  PRIMARY KEY(upc, store_id),
  FOREIGN KEY (upc) REFERENCES product(upc),
  CHECK (item_count <= capacity)
);

CREATE TABLE store (
  store_id int AUTO_INCREMENT,
  country char(3) NOT NULL,
  region varchar(20),
  address varchar(30) NOT NULL,
  zip_code int NOT NULL,
  phone_number varchar(15) UNIQUE,
  PRIMARY KEY (store_id)
);

CREATE TABLE hours (
  store_id int,
  weekday char(3), -- MON, TUE, WED, etc.
  open_at time,
  close_at time,
  closed bit DEFAULT 0,
  PRIMARY KEY (store_id, weekday),
  FOREIGN KEY (store_id) REFERENCES store(store_id)
);

CREATE TABLE store_order_items (
  reorder_id int AUTO_INCREMENT,
  store_id int,
  upc int,
  order_qty int,
  fulfillment_status bit DEFAULT 0,
  cost decimal(9,2),
  PRIMARY KEY (reorder_id),
  FOREIGN KEY (store_id) REFERENCES store(store_id),
  FOREIGN KEY (upc) REFERENCES product(upc)
);

CREATE TABLE incoming_shipments (
  shipment_id int AUTO_INCREMENT,
  expected_arrival_date date,
  actual_arrival_date date,
  PRIMARY KEY (shipment_id)
);

CREATE TABLE shipment_items (
  shipment_id int,
  upc int,
  quantity int,
  PRIMARY KEY (shipment_id, upc),
  FOREIGN KEY (shipment_id) REFERENCES incoming_shipments(shipment_id),
  FOREIGN KEY (upc) REFERENCES product(upc)
);

CREATE TABLE customers (
  customer_id int AUTO_INCREMENT,
  c_name varchar(25) NOT NULL,
  c_email varchar(30) UNIQUE,
  c_phone varchar(15) UNIQUE,
  PRIMARY KEY (customer_id)
);

CREATE TABLE online_order (
  online_order_id int AUTO_INCREMENT,
  order_status varchar(30),
  customer_id int NOT NULL,
  store_id int NOT NULL,
  PRIMARY KEY (online_order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (store_id) REFERENCES store(store_id)
);

CREATE TABLE online_order_items (
  online_order_id int,
  upc int,
  order_qty int NOT NULL,
  purchase_price decimal(9,2),
  PRIMARY KEY (online_order_id, upc),
  FOREIGN KEY (upc) REFERENCES product(upc)
);

CREATE TABLE local_order (
  local_order_id int AUTO_INCREMENT,
  customer_id int, -- Nulls allowed since customers can check out without an account
  store_id int NOT NULL,
  PRIMARY KEY (local_order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (store_id) REFERENCES store(store_id)
);

CREATE TABLE local_order_items (
  local_order_id int,
  upc int,
  order_qty int NOT NULL,
  purchase_price decimal(9,2), -- Price actually paid Needs to be stored since prices might change 
  PRIMARY KEY (local_order_id, upc),
  FOREIGN KEY (upc) REFERENCES product(upc)
);