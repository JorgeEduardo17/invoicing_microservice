-- init_db.sql

-- Crea la base de datos si no existe
CREATE DATABASE invoicedb;

-- Conéctate a la base de datos recién creada
\c invoicedb;

-- Creación de la tabla Person
CREATE TABLE IF NOT EXISTS Person (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    identification VARCHAR(100) NOT NULL UNIQUE
);

-- Creación de la tabla Product
CREATE TABLE IF NOT EXISTS Product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    unit_of_measure VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    description TEXT
);

-- Creación de la tabla Invoice
CREATE TABLE IF NOT EXISTS Invoice (
    id SERIAL PRIMARY KEY,
    person_id INTEGER REFERENCES Person(id),
    sequential_number INTEGER NOT NULL,
    date DATE NOT NULL
);

-- Creación de la tabla InvoiceDetail
CREATE TABLE IF NOT EXISTS InvoiceDetail (
    id SERIAL PRIMARY KEY,
    invoice_id INTEGER REFERENCES Invoice(id),
    product_id INTEGER REFERENCES Product(id),
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL
);

-- Insertar datos de ejemplo en la tabla Person
INSERT INTO Person (name, identification) VALUES
('John Doe', '1234567890'),
('Jane Smith', '2345678901'),
('Alice Johnson', '3456789012'),
('Bob Brown', '4567890123'),
('Carol White', '5678901234');

-- Insertar datos de ejemplo en la tabla Product
INSERT INTO Product (name, unit_of_measure, price, description) VALUES
('Milk', 'Liter', 1.50, 3.0, 'Organic whole milk'),
('Bread', 'Piece', 2.00, 1.5, 'Freshly baked wheat bread'),
('Eggs', 'Dozen', 3.00, 2.0, 'Free-range eggs'),
('Apples', 'Kilogram', 2.50, 3.0, 'Red apples'),
('Rice', 'Kilogram', 1.00, 1.5, 'Long-grain rice');

-- Insertar datos de ejemplo en la tabla Invoice
INSERT INTO Invoice (person_id, sequential_number, date) VALUES
(1, 1001, '2024-01-10'),
(2, 1002, '2024-01-11'),
(3, 1003, '2024-01-12'),
(4, 1004, '2024-01-13'),
(5, 1005, '2024-01-14');

-- Insertar datos de ejemplo en la tabla InvoiceDetail
INSERT INTO InvoiceDetail (invoice_id, product_id, quantity, unit_price) VALUES
(1, 1, 2, 1.50),
(1, 2, 1, 2.00),
(2, 3, 2, 3.00),
(3, 4, 3, 2.50),
(4, 5, 4, 1.00);

-- Creación de las vistas solicitadas

-- Vista para el total facturado por persona
CREATE VIEW TotalInvoicedPerPerson AS
SELECT p.id, p.name, SUM(d.quantity * d.unit_price) AS total_invoiced
FROM Person p
JOIN Invoice i ON p.id = i.person_id
JOIN InvoiceDetail d ON i.id = d.invoice_id
GROUP BY p.id, p.name;

-- Vista para la persona que compró el producto más caro
CREATE VIEW PersonWithMostExpensivePurchase AS
SELECT p.id, p.name, MAX(d.unit_price) AS highest_price
FROM Person p
JOIN Invoice i ON p.id = i.person_id
JOIN InvoiceDetail d ON i.id = d.invoice_id
GROUP BY p.id, p.name
ORDER BY highest_price DESC
LIMIT 1;

-- Vista para los productos ordenados por cantidad facturada
CREATE VIEW ProductsOrderedByInvoicedAmount AS
SELECT pr.id, pr.name, SUM(d.quantity) AS total_quantity
FROM Product pr
JOIN InvoiceDetail d ON pr.id = d.product_id
GROUP BY pr.id, pr.name
ORDER BY total_quantity DESC;

-- Vista para los productos ordenados por utilidad generada
CREATE VIEW ProductsOrderedByProfitGenerated AS
SELECT pr.id, pr.name, SUM((d.unit_price - pr.cost) * d.quantity) AS total_profit
FROM Product pr
JOIN InvoiceDetail d ON pr.id = d.product_id
GROUP BY pr.id, pr.name
ORDER BY total_profit DESC;

-- Vista para los productos y margen de ganancia
CREATE VIEW ProductAndProfitMargin AS
SELECT pr.id, pr.name, (pr.price - pr.cost) AS profit_margin
FROM Product pr;
