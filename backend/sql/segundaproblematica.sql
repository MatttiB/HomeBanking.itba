																/*Segunda Problematica*/
																
/*Crear una vista con las columnas id, numero sucursal, nombre, apellido, DNI y edad de la tabla cliente calculada a partir de la fecha de nacimiento*/

/*Mostrar las columnas de los clientes, ordenadas por el DNI de menor a mayor y cuya edad sea superior a 40 años*/
SELECT customer_id, branch_number, customer_name,customer_surname, customer_DNI, CAST(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', dob ) as int) AS Edad
FROM cliente
INNER JOIN sucursal
ON cliente.branch_id = sucursal.branch_id
WHERE edad>40 
ORDER BY customer_DNI ASC

/*Mostrar todos los clientes que se llaman “Anne” o “Tyler” ordenados por edad de menor a mayor*/
SELECT customer_id, branch_number, customer_name,customer_surname, customer_DNI, CAST(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', dob ) as int) AS Edad
FROM cliente
INNER JOIN sucursal
ON cliente.branch_id = sucursal.branch_id
WHERE customer_name='Tyler' OR customer_name='Anne'
ORDER BY edad ASC

/*Insertar 5 nuevos clientes en la base de datos y verificar que se haya realizado con éxito la inserción*/
/*1*/
INSERT INTO cliente (customer_name, customer_surname, customer_DNI, dob, branch_id)
VALUES ('Lois', 'Stout', 47730534, '1984-07-07', 80);
/*2*/
INSERT INTO cliente (customer_name, customer_surname, customer_DNI, dob, branch_id)
VALUES ('Hall', 'Mcconnell',52055464, '1968-04-30', 45);
/*3*/
INSERT INTO cliente (customer_name, customer_surname, customer_DNI, dob, branch_id)
VALUES ('Jin', 'Cooley', 21207908, '1959-08-24', 96);
/*4*/
INSERT INTO cliente (customer_name, customer_surname, customer_DNI, dob, branch_id)
VALUES ('Hilel', 'Mclean', 43625213, '1993-03-28',  77);
/*5*/
INSERT INTO cliente (customer_name, customer_surname, customer_DNI, dob, branch_id)
VALUES ('Gabriel', 'Harmon',57063950,'1976-04-01',27);

/*Consulta de tabla cliente para verificar la insercion*/
SELECT *
FROM cliente

/*Actualizar 5 clientes recientemente agregados en la base de datos dado que hubo un error en el JSON que traía la información, la sucursal de todos es la 10*/
UPDATE cliente
SET branch_id = 10
WHERE customer_id = 501 OR customer_id = 502 OR customer_id = 503 OR customer_id = 504 OR customer_id = 505;

/*Eliminar el registro correspondiente a “Noel David” realizando la selección por el nombre y apellido*/
DELETE FROM cliente
WHERE customer_name='Noel' AND customer_surname='David';

/*Consultar sobre cuál es el tipo de préstamo de mayor importe*/
SELECT loan_id, loan_type, MAX (loan_total) as Mayor_Importe
FROM prestamo;

/*Para corroborar que este bien el mayor importe*/
SELECT *
FROM prestamo
ORDER BY loan_total DESC
LIMIT 10;


