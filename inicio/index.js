const TIPO_DOLAR = ["Dolar Oficial", "Dolar Blue", "Dolar Contado con Liqui"];
const OFICIAL = 0,
    BLUE = 1,
    LIQUI = 2;

function agregarOficial(compra, venta){
    const dolarOficialCompra = document.getElementById("dolar-oficial-compra");
    const dolarOficialVenta = document.getElementById("dolar-oficial-venta");

    dolarOficialCompra.appendChild(compra);
    dolarOficialVenta.appendChild(venta);
}

function agregarBlue(compra, venta){
    const dolarBlueCompra = document.getElementById("dolar-blue-compra");
    const dolarBlueVenta = document.getElementById("dolar-blue-venta");

    dolarBlueCompra.appendChild(compra);
    dolarBlueVenta.appendChild(venta);
}

function agregarLiqui(compra, venta){
    const dolarLiquiCompra = document.getElementById("dolar-liqui-compra");
    const dolarLiquiVenta = document.getElementById("dolar-liqui-venta");

    dolarLiquiCompra.appendChild(compra);
    dolarLiquiVenta.appendChild(venta);
}

fetch("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    .then(data => data.json())
    .then(data => {
        for(let elemento of data){
            let tipoDeDolar = elemento.casa.nombre;
            let compra = document.createElement("p");
            let venta = document.createElement("p");

            compra.innerText = `$${elemento.casa.compra}`;
            venta.innerText = `$${elemento.casa.venta}`;

            if(tipoDeDolar == TIPO_DOLAR[OFICIAL]){ 
                agregarOficial(compra, venta);               

            }else if (tipoDeDolar == TIPO_DOLAR[BLUE]){
                agregarBlue(compra, venta);

            } else if(tipoDeDolar == TIPO_DOLAR[LIQUI]){
                agregarLiqui(compra, venta);
            }
        }
    })

//Desplegable de actividad reciente
    $(".desplegable > ").click(function() {      
        $(this).next(".contenido").toggle(500);
      });