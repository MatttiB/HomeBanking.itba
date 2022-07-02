import argparse, csv
from datetime import datetime

VACIO = "*****"

# CONSTANTES 

ETIQUETA_CABECERA_CSV_DNI = "DNI"
ETIQUETA_CABECERA_CSV_NUM_CHEQUE = "NroCheque"
ETIQUETA_CABECERA_CSV_FECHA = "Fecha"
ETIQUETA_CABECERA_CSV_CUENTA = "NroCuenta"
ETIQUETA_CABECERA_CSV_VALOR = "Valor"
ETIQUETA_CABECERA_CSV_TIPO = "Tipo"
ETIQUETA_CABECERA_CSV_ESTADO = "Estado"
ETIQUETA_CABECERA_CSV_FECHA_ORIGEN = "FechaOrigen"
ETIQUETA_CABECERA_CSV_FECHA_PAGO = "FechaPago"
ETIQUETA_CABECERA_CSV_NUM_CUENTA = "NumeroCuentaOrigen"

# EN LUGAR DE USAR EL ".SYS" UTILIZAMOS EL METODO ".PARSER' QUE ES MAS AMIGABLE Y PERMITE DELIMITAR EL TIPO DE ENTRADA

parser = argparse.ArgumentParser(description= "Buscador de cheques")

parser.add_argument('NOMBRE_ARCHIVO', type=str, help='El nombre del archivo en el que se tiene que buscar')
parser.add_argument('DNI', type=int, help='DNI del usuario a buscar')
parser.add_argument('SALIDA', type=str, choices=['pantalla', 'csv'], default='csv',help='Por donde se muestra la información ( PANTALLA o CSV )')
parser.add_argument('TIPO', type=str,choices=['EMITIDO', 'DEPOSITADO'], help='El tipo de cheque que se busca')
parser.add_argument('-e', '--estado', type=str, choices=['PENDIENTE', 'APROBADO', 'RECHAZADO'], default=VACIO, help='En que estado esta el cheque que se busca')
parser.add_argument('-r', '--rango', type=str, default=VACIO, help='El rango de fechas dentro del que se tiene que buscar')

args = parser.parse_args()

if __name__ == "__main__":
    
    with open(args.NOMBRE_ARCHIVO) as archivo:
        lector = csv.reader(archivo)
        datos = list(lector)
        
    cabecera = datos[0]

    #CABECERA DEL CSV

    (posicion_dni,
     posicion_numero,
     posicion_tipo,
     posicion_estado,
     posicion_fecha_origen,
     posicion_fecha_pago,
     posicion_valor,
     posicion_num_cuenta) = (cabecera.index(ETIQUETA_CABECERA_CSV_DNI),
                         cabecera.index(ETIQUETA_CABECERA_CSV_NUM_CHEQUE),
                         cabecera.index(ETIQUETA_CABECERA_CSV_TIPO),
                         cabecera.index(ETIQUETA_CABECERA_CSV_ESTADO),
                         cabecera.index(ETIQUETA_CABECERA_CSV_FECHA_ORIGEN),
                         cabecera.index(ETIQUETA_CABECERA_CSV_FECHA_PAGO),
                         cabecera.index(ETIQUETA_CABECERA_CSV_VALOR),
                         cabecera.index(ETIQUETA_CABECERA_CSV_NUM_CUENTA))
    
    datos_cliente = list(filter(lambda registro:
                                    registro[posicion_dni] == str(args.DNI) and registro[posicion_tipo] == args.TIPO, datos[1:]))
    
    numeros_cheques = []
    repetidos = []
    
    #SE VERIFICA QUE SE CUENTEN Y QUE NO ESTEN REPETIDOS LOS CHEQUES 
    for cheques in datos_cliente:
        
        if numeros_cheques.count(cheques[posicion_numero]) == 1:
        
            repetidos.append(cheques[posicion_numero])
            
        else:
        
            numeros_cheques.append(cheques[posicion_numero])
    
    if repetidos != []:
    
        print("Hay cheques con el mismo número de cheque")
    
    else:
    
        #FILTRA POR EL ESTADO DEL CHEQUE SI ES QUE SE PASA POR PARAMETRO
        if args.estado != VACIO:
        
            datos_cliente = list(filter(lambda registro:
                                    registro[posicion_estado] == args.estado, datos_cliente))
    
        #FILTRA POR RANGO DE FECHA DE ORIGEN DEL CHEQUE SI SE INGRESA POR PARAMETRO    
        if args.rango != VACIO:
        
            fecha_menor = args.rango[6:10] + "-" + args.rango[3:5] + "-" + args.rango[:2]
            fecha_mayor = args.rango[17:] + "-" + args.rango[14:16] + "-" + args.rango[11:13]
  
            nuevos_datos = []
        
            for cheque in datos_cliente:
            
                fecha_cheque = cheque[posicion_fecha_origen]
                fecha = datetime(int(fecha_cheque[4:]), int(fecha_cheque[2:4]), int(fecha_cheque[:2]))
            
                if str(fecha) > fecha_menor and str(fecha) < fecha_mayor:
                
                    nuevos_datos.append(cheque)
                
            datos_cliente = nuevos_datos

        # CORROBORA SI SE PIDE QUE SE IMPRIMA POR PANTALLA O SE PASE EL ARCHIVO CSV
        if args.SALIDA == "pantalla":
        
            print(",".join(cabecera))
            for cheque in datos_cliente:
                print(",".join(cheque))
    
        else:
        
            now = datetime.now()
            nombre_archivo = str(args.DNI) + "_" + str(now.day) + "-" + str(now.month) + "-" + str(now.year) + ".csv"
        
            with open(nombre_archivo, "w") as archivo:
            
                archivo.write(cabecera[posicion_fecha_origen] + "," + cabecera[posicion_fecha_pago] + "," + cabecera[posicion_valor] + "," + cabecera[posicion_num_cuenta] + "\n")
                
                for cheque in datos_cliente:
                    archivo.write(cheque[posicion_fecha_origen] + "," + cheque[posicion_fecha_pago] + "," + cheque[posicion_valor] + "," + cheque[posicion_num_cuenta] + "\n")