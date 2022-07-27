/*Tipo De Cliente*/
CREATE TABLE tipo_cliente(
				tipo_id INTEGER PRIMARY KEY,
				tipo_name TEXT NOT NULL
				);

INSERT INTO tipo_cliente (tipo_name)
VALUES ('Classic'), ('Gold'), ('Black');

SELECT *
FROM tipo_cliente;				

CREATE TABLE cuenta(
				account_id INTEGER NOT NULL PRIMARY KEY,
				customer_id INTEGER NOT NULL,
				balance INTEGER NOT NULL,
				cuenta_id INTEGER NOT NULL,
				tipo_tarjeta
				customer_id INTEGER NOT NULL,
				FOREIGN KEY (customer_id)
				REFERENCES cuenta (customer_id)
				);
/*Para agregar una columna a una tabla existente*/
ALTER TABLE table_name
ADD COLUMN column_definition;

/*Tipo De Cuenta*/
CREATE TABLE tipo_cuenta(
				cuenta_id INTEGER PRIMARY KEY,
				cuenta_name TEXT NOT NULL
				);

INSERT INTO tipo_cuenta (cuenta_name)
VALUES ('Caja de ahorro en pesos'), ('Caja de ahorro en dolares'), ('Cuenta corriente');

SELECT *
FROM tipo_cuenta;			

/*Marcas de tarjetas*/
CREATE TABLE marca_tarjeta(
				tarjeta_id INTEGER PRIMARY KEY,
				tarjeta_name TEXT NOT NULL
				);

INSERT INTO marca_tarjeta (tarjeta_name)
VALUES ('VISA'), ('MASTERCARD'), ('AMEX'), ('CABAL');

SELECT *
FROM marca_tarjeta	

SELECT *
FROM cuenta

/*Agregado entidad tarjeta*/ /*Relacionado de tarjetas con la tabla donde se guardan las marcas de tarjeta y con el cliente al que pertenecen*/
CREATE TABLE tarjeta( 
				numero INTEGER NOT NULL PRIMARY KEY CHECK(length(numero) <= 20),
				cvv INTEGER NOT NULL,
				fecha_de_otorgamiento INTEGER NOT NULL,
				fecha_de_expiracion INTEGER NOT NULL,
				tipo_tarjeta INTEGER NOT NULL,
				tarjeta_id INTEGER NOT NULL,
				customer_id INTEGER NOT NULL,
				FOREIGN KEY (customer_id)
				REFERENCES cuenta (customer_id)
				FOREIGN KEY (tarjeta_id)
				REFERENCES marca_tarjeta (tarjeta_id)
				);
/*Agregar 500 tarjetas de credito*/
INSERT INTO tarjeta (numero)
VALUES ('6545123547895245'); /*Aca agregamos 500 numeros aleatorios de tarjeta y asi con el resto*/

				
/*Agregado entidad direcciones*/
CREATE TABLE direcciones( 
				numero INTEGER NOT NULL PRIMARY KEY CHECK(length(numero) <= 20),
				cvv INTEGER NOT NULL,
				fecha_de_otorgamiento INTEGER NOT NULL,
				fecha_de_expiracion INTEGER NOT NULL,
				customer_id INTEGER NOT NULL,
				FOREIGN KEY (customer_id)
				REFERENCES cuenta (customer_id)
				);

/*Agregar 500 direcciones*/
INSERT INTO marca_tarjeta (tarjeta_name)
VALUES ('VISA'), ('MASTERCARD'), ('AMEX'), ('CABAL');

/*Amplio alcance entidad cuenta  para que identifique el tipo de la misma*/ /*Hay que agregar tipo_cuenta*/ 
ALTER TABLE cuenta
ADD COLUMN tipo_de_cuenta INTEGER NOT NULL; /*Hay que fijarse como hacer para relacionar con tipo_cuenta*/

/*Asignar un tipo de cuenta a cada registro de cuenta de forma aleatoria*/
INSERT INTO marca_tarjeta (tarjeta_name)
VALUES ('VISA'), ('MASTERCARD'), ('AMEX'), ('CABAL');
UPDATE 

/*Consulta tabla empleado*/ 
SELECT * 
FROM empleado

/*Corregir el campo employee_hire_date de la tabla empleado con la fecha en formato YYYY-MM-DD*/
