-- Customer table
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    age INT
);


-- Sales table
CREATE TABLE Sales (
    sales_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

-- Items table
CREATE TABLE Items (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(255)
);

-- Orders table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    sales_id INT,
    item_id INT,
    quantity INT,
    FOREIGN KEY (sales_id) REFERENCES Sales(sales_id),
    FOREIGN KEY (item_id) REFERENCES Items(item_id)
);


-- Inserting data into Customer table
INSERT INTO Customer (customer_id, age) VALUES
(1, 30),
(2, 25),
(3, 35);

-- Inserting data into Sales table
INSERT INTO Sales (sales_id, customer_id) VALUES
(101, 1),
(102, 2),
(103, 3);

-- Inserting data into Items table for electronics
INSERT INTO Items (item_id, item_name) VALUES
(1, 'Laptop'),
(2, 'Smartphone'),
(3, 'Tablet');

-- Inserting data into Orders table
INSERT INTO Orders (order_id, sales_id, item_id, quantity) VALUES
(1001, 101, 1, 2),   -- 2 laptops sold in sale 101
(1002, 102, 2, 3),   -- 3 smartphones sold in sale 102
(1003, 103, 3, 1);   -- 1 tablet sold in sale 103;

