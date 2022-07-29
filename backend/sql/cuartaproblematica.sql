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

/*Obtener la cantidad de tarjetas de crédito por tipo por sucursal*/
SELECT idtarjeta, qtarjeta, idBranch
FROM ( SELECT sucursal.branch_id as idBranch, COUNT(tarjeta.tipo_tarjeta) as qtarjeta, tarjeta.tarjeta_id as idtarjeta
		FROM sucursal, tarjeta
		LEFT JOIN cliente
		ON sucursal.branch_id = cliente.branch_id
		
		LEFT JOIN (
			SELECT tarjeta.customer_id as idtar, cliente.customer_id
			FROM tarjeta
			LEFT JOIN cliente
			ON tarjeta.customer_id = cliente.customer_id
			GROUP BY tarjeta.customer_id
		) as tarjetas_customerid
		ON sucursal.branch_id = tarjetas_customerid.idtar
		GROUP BY sucursal.branch_id
);

SELECT*
FROM tarjeta

COUNT(tipo_tarjeta), tarjeta_id, branch_id
tipo_tarjeta = 'Credito'
tarjeta.customer_id = cliente.customer_id /**/ cliente.branch_id = sucursal.branch_id
/*Relaciono tarjeta con cliente y cliente con sucursal para llegar a relacion tarjeta-sucursal*/