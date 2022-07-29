/*Seleccion de cuentas con saldo negativo*/
SELECT *
FROM cuenta
WHERE balance<0;

/*Seleccion datos de clientes con apellidos que contengan z*/
SELECT cliente.customer_name, cliente.customer_surname, CURRENT_DATE - dob AS Edad_cliente
FROM cliente
WHERE customer_surname LIKE '%z%' ;
 
/*Seleccion datos de clientes y sucursal cuyo nombre sea Brendan*/
SELECT customer_name, customer_surname, CURRENT_DATE - dob AS Edad_cliente, branch_name AS Nom_Sucursal
FROM (		
		SELECT *
		FROM cliente
		INNER JOIN sucursal ON cliente.branch_id = sucursal.branch_id
		)

WHERE customer_name = 'Brendan' 
ORDER BY branch_name; 


/*Seleccion prestamos prendarios y con importe mayor a $80000*/

SELECT * 
FROM prestamo
WHERE loan_total > 8000000
	UNION
SELECT * 
FROM prestamo
WHERE loan_type= 'PRENDARIO';



/*Seleccion prestamos cuyo importe sea mayor que el promedio*/

SELECT *
FROM prestamo
WHERE loan_total > (SELECT avg(loan_total) FROM prestamo);

/*Consultar promedio*/
SELECT avg(loan_total)
FROM prestamo;


/*Cantidad de clientes menores de 50*/
SELECT COUNT(Edad_cliente)
FROM(
	 SELECT CURRENT_DATE - dob AS Edad_cliente
	From cliente)
WHERE Edad_cliente <50;


/*Seleccionar las 5 primeras cuentas con saldo mayor a $8000*/
SELECT *
FROM cuenta
WHERE balance > 800000
LIMIT 5;

/*Seleccionar los prestamos que tengan fecha en abril, junio y agosto*/
SELECT * 
FROM prestamo 
WHERE strftime('%m', loan_date) = '04' 
	UNION
SELECT * 
FROM prestamo 
WHERE strftime('%m', loan_date) = '06'
	UNION
SELECT * 
FROM prestamo 
WHERE strftime('%m', loan_date) = '08'
ORDER BY loan_total;


/*Importe total de los prestamos*/
SELECT loan_type, sum(loan_total) AS loan_total_accu
FROM prestamo
GROUP BY loan_type;

