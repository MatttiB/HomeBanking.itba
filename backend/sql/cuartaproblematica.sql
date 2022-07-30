																/*Cuarta Problematica*/
/*Listar la cantidad de clientes por nombre de sucursal ordenando de mayor a menor*/
SELECT COUNT(customer_id) as Cant_Clientes, branch_name
FROM cliente
INNER JOIN sucursal
ON cliente.branch_id = sucursal.branch_id
GROUP BY branch_name
ORDER BY Cant_Clientes DESC;

/*Obtener la cantidad de empleados por cliente por sucursal en un número real*/
SELECT idBranch, qClientes, qEmpleados, round((qClientes*1.0/qEmpleados*1.0), 2) as q
FROM ( SELECT sucursal.branch_id as idBranch, count(cliente.customer_id) as qClientes, qEmpleados
		FROM sucursal
		LEFT JOIN cliente
		ON sucursal.branch_id = cliente.branch_id
		
		LEFT JOIN (
			SELECT sucursal.branch_id as sucursalID, count(empleado.employee_id) as qEmpleados
			FROM sucursal
			LEFT JOIN empleado
			ON sucursal.branch_id = empleado.branch_id
			GROUP BY sucursal.branch_id
		) as cantidad_Empleados
		ON sucursal.branch_id = cantidad_Empleados.sucursalID
		GROUP BY sucursal.branch_id
) as Division;

/*Obtener la cantidad de tarjetas de crédito por tipo por sucursal que la entrego*/
SELECT COUNT(tarjeta.tipo_tarjeta) as Cant_tarjetas, tarjeta_id as tipo_de_tarjeta, branch_id as Nro_Sucursal
FROM tarjeta
GROUP BY tarjeta_id;

/*Esto es para comprobar y ver que cada columna este bien*/
SELECT*
FROM tarjeta;

/*Obtener el promedio de créditos otorgado por sucursal*/
SELECT COUNT (loan_type) as Promedio, loan_type as tipo_credito, branch_id as Sucursal
FROM prestamo
GROUP BY loan_type;

/*Crear una tabla denominada “auditoria_cuenta” para guardar los datos movimientos*/
CREATE TABLE auditoria_cuenta(
			old_id INTEGER PRIMARY KEY,
			new_id INTEGER,
			old_balance INTEGER,
			new_balance INTEGER, 
			old_iban TEXT,
			new_iban TEXT,
			old_type INTEGER,
			new_type INTEGER, 
			user_action INTEGER,
			created_at INTEGER
			);

/*Crear un trigger que después de actualizar en la tabla cuentas los campos balance, IBAN o tipo de cuenta registre en la tabla auditoria*/
CREATE TRIGGER registro_auditoria
AFTER UPDATE ON cliente
WHEN OLD.balance <> NEW.balance <> OLD.iban != NEW.iban <> OLD.tipo_de_cuenta <> NEW.tipo_de_cuenta
BEGIN
	INSERT INTO auditoria_cuenta(
			old_id,
			new_id,
			old_balance,
			new_balance, 
			old_iban,
			new_iban,
			old_type,
			new_type, 
			user_action,
			created_at
	)
VALUES 
	(	old.id,
		new.id,
		old.balance,
		new.balance, 
		old.iban,
		new.iban,
		old.type,
		new.type, 
		'UPDATE',
		DATETIME('NOW')
	);
END;

/* Restar $100 a las cuentas 10,11,12,13,14*/
UPDATE cuenta
SET balance = balance - 100
WHERE account_id = 14; /*Asi para las distintas cuentas*/

/*Para comprobar que se actualizo los balances*/
SELECT *
FROM cuenta

/*Mediante índices mejorar la performance la búsqueda de clientes por DNI*/
CREATE UNIQUE INDEX clientes_x_dni
ON cliente (customer_DNI); /*ver*/

/*Crear la tabla “movimientos” con los campos de identificación del movimiento, número de cuenta, monto, tipo de operación y hora*/
CREATE TABLE movimientos (
			movimiento INTEGER NOT NULL PRIMARY KEY,
			nro_cuenta INTEGER NOT NULL, 
			flag TEXT NOT NULL,
			monto INTEGER NOT NULL,
			tipo_operacion INTEGER NOT NULL DEFAULT 'Transaccion',
			hora TIME NOT NULL
			);

/*Mediante el uso de transacciones, hacer una transferencia de 1000$ desde la cuenta 200 a la cuenta 400*/
/*Registrar el movimiento en la tabla movimientos*/
BEGIN TRANSACTION;

UPDATE cuenta
   SET balance = balance - 1000
 WHERE account_id = 200;

UPDATE cuenta
   SET balance = balance + 1000
 WHERE account_id = 400;
 
INSERT INTO movimientos (nro_cuenta,flag,monto, hora) 
VALUES(200,'-',1000,datetime('now'));

INSERT INTO movimientos (nro_cuenta,flag,monto,hora) 
VALUES(400,'+',1000,datetime('now'));

COMMIT;


/*Consulto movimientos*/
SELECT *
FROM movimientos

/*En caso de no poder realizar la operación de forma completa, realizar un ROLLBACK*/
BEGIN TRANSACTION;

UPDATE cuenta
   SET balance = balance - 1000
 WHERE account_id = 400;

INSERT INTO movimientos(nro_cuenta,flag,monto,hora)
VALUES(400,'-',1000,datetime('now'));

ROLLBACK;
