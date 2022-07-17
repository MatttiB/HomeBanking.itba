class Reporte:
    def __init__(self, cliente):
        with open('reporte.html', 'w') as reporte:

            html_template = """
            <html>
                <head>
                <title>Reporte Final</title>
                </head>
                <body style="background-color:#0e6da8 ; font-family: Helvetica, Sans-Serif">
                    <h1 style="text-align:center">Reporte del usuario</h1>
                    <form name="form-1">
                        <table width = 55% border="1" align="center" style="background-color:white; text-align:center">
                            <tr>
                                <td colspan="2">
                                    <div align="center"><strong>Datos del cliente</strong></div>
                                </td>
                            </tr>
                            <tr>
                                <td>Nombre del cliente</td>
                                <td>{}</td>
                            </tr>
                            <tr>
                                <td>Numero</td>
                                <td>{}</td>
                            </tr>
                            <tr>
                                <td>DNI</td>
                                <td>{}</td>
                            </tr>
                            <tr>
                                <td>Direccion</td>
                                <td>{}</td>
                            </tr>
                        </table>
                    </form>      
                </body>
            </html>
            """.format(cliente.obtener_nombre(), cliente.obtener_numero(),cliente.obtener_dni() , cliente.obtener_direccion())

            reporte.write(html_template)

    def crear_reporte(self, transaccion, error):

        with open('reporte.html', 'a') as reporte:

            html_template = """
                <form name="form-1">
                    <table width = 55% border="1" align="center" style="background-color:white; text-align:center">
                        <td colspan="2">
                            <div align="center"><strong>Datos de transaccion</strong></div>
                        </td>
                        <tr>
                            <td>Fecha de transaccion</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>Tipo de operacion</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>Estado</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>Monto</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>Razon de rechazo</td>
                            <td>{}</td>
                        </tr>
                    </table>
                </form>
            """.format(transaccion["fecha"], transaccion["tipo"], transaccion["estado"], transaccion["monto"], error)

            reporte.write(html_template)
