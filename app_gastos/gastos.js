var montoTotal = 0;
var participantes = 0;


function crearElemento(nombre, monto){

    var contribuyentes = document.getElementById("contribuyentes");
    var pEjemplo = document.getElementById("p-ejemplo");
    var p = pEjemplo.cloneNode(true);

    p.innerHTML = nombre + ": " + "$" + monto;

    p.style.setProperty("padding", "none");

    contribuyentes.appendChild(p);
}

function actualizarResumen(){
    const montoFinal = document.getElementById("monto-total");
    const montoDividido = document.getElementById("monto-dividido");

    montoFinal.textContent = "TOTAL: $" + montoTotal;
    montoDividido.textContent = "A cada uno le toca aportar: $" + (montoTotal / participantes);
}

function agregar(){

    const nombre = document.getElementById("nombre");
    const monto = document.getElementById("monto");
    var nombreAgregado = nombre.value;
    var montoAgregado= monto.value;

    if(nombreAgregado===''||montoAgregado===''){
        nombre.setAttribute('placeholder', 'agregar un nombre válido');
        monto.setAttribute('placeholder', 'agregar un monto válido');
        return false;
        
    }
    
    crearElemento(nombre.value, monto.value);

    montoTotal += parseFloat(monto.value);
    participantes++;

    actualizarResumen();

    nombre.value =  "";
    monto.value = "";
    nombre.setAttribute('placeholder', 'Nombre');
    monto.setAttribute('placeholder', 'Monto');
    
}

