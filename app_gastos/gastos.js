var montoTotal = 0;
var participantes = 0;


function crearElemento(nombre, monto){

    var contribuyentes = document.getElementById("contribuyentes");
    var pEjemplo = document.getElementById("p-ejemplo");
    var p = pEjemplo.cloneNode(true);
    
    p.onclick=quitar;

    p.innerHTML = nombre + ": " + "$" + monto;

    p.style.setProperty("padding", "none");

    contribuyentes.appendChild(p);
}

function actualizarResumen(){
    const montoFinal = document.getElementById("monto-total");
    const montoDividido = document.getElementById("monto-dividido");

    montoFinal.textContent = "TOTAL: $" + montoTotal;
    montoDividido.textContent = "A cada uno le toca aportar: $" + (montoTotal / participantes);

    quitar();

}

function setErrorFor(input, message) {
const formControl = input.parentElement;
const small = formControl.querySelector('small');
formControl.className = 'form-control error';
small.innerText = message;

}

function setSuccessFor(input) {
const formControl = input.parentElement;
formControl.className = 'form-control success';
}

function agregar(){

    const nombre = document.getElementById("nombre");
    const monto = document.getElementById("monto");
    var nombreAgregado = nombre.value;
    var montoAgregado= monto.value;


    if(nombreAgregado===''&&montoAgregado===''){
        nombre.setAttribute('placeholder', 'Agregar un nombre válido');
        monto.setAttribute('placeholder', 'Agregar un monto válido');
        setErrorFor(nombre, 'Debe completar este campo');
        setErrorFor(monto, 'Debe completar este campo')
        return false;}
        

    if(nombreAgregado===''){
        nombre.setAttribute('placeholder', 'Agregar un nombre válido');
        setErrorFor(nombre, 'Debe completar este campo');
        return false;
        }

    if(montoAgregado===''){
        monto.setAttribute('placeholder', 'Agregar un monto válido');
        setErrorFor(monto, 'Debe completar este campo')
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
    setSuccessFor(monto);
    setSuccessFor(nombre);
}
    
function quitar () {
    document.getElementById('contribuyentes').removeChild(this);

    montoTotal -= parseFloat (monto.value);
   
    if (montoTotal<=0) {
        contribuyentes.setAttribute('placeholder', 'A cada uno le toca aportar');
    }
    
    actualizarResumen();
    agregar();

}

