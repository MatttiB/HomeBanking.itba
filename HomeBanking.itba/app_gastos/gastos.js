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

function sololetras(e){
    key=e.keyCode || e.which;
    teclado=String.fromCharCode(key).toLowerCase();
    letras=" abcdefghijklmnñopqrstuvwxyz";
    especiales="8-37-38-46-164";
    teclado_especial=false;
    for(var i in especiales){
        if(key==especiales[i]){
            teclado_especial=true;break;
        }
    }
    if(letras.indexOf(teclado)==-1 && !teclado_especial){
        return false;
    }
}

