function armarNombre(cadena){
    let armadoNombre = "";
    
    for(var j = 0; cadena[j] != ":" ; j++){
        armadoNombre += cadena[j];
    }

    return armadoNombre;
}

function buscarNombre(nombre, lista){
    let index;
    for(var i = 0; i < lista.length; i++){
        if(lista[i][0] == nombre){
            index = i;
        }
    }
    return index
}

function actualizarResumen(montoTotal, participantes){
    const total = document.getElementById("monto-total"),
        montoParticipante = document.getElementById("monto-dividido");

    total.textContent = "TOTAL: $" + montoTotal;
    montoParticipante.textContent = "A cada uno le toca aportar: $" + (montoTotal/participantes);
}

(function(){
    const nombre = document.getElementById("nombre"),
        monto = document.getElementById("monto"),
        boton = document.getElementById("boton");

    let montoTotal = 0;
    let participantes = 0;

    let listaParticipantes = [];
    
    const agregarMonto = function(){
        if (nombre.value == "" || isNaN(monto.value) || monto.value == ""){

            if (nombre.value == ""){
                nombre.value = "";
                nombre.setAttribute("placeholder" , "Ingrese un nombre válido");
                nombre.className = "form-control w-50 mb-2 border-danger";
            } 
            if(isNaN(monto.value) || monto.value == "") {
                monto.value = "";
                monto.setAttribute("placeholder" , "Ingrese un monto válido");
                monto.className = "form-control w-50 mb-2 border-danger";  
            }

        }else {

            const contribuyentes = document.getElementById("contribuyentes");

            const p = document.createElement("p");
            p.textContent = nombre.value + ": $" + monto.value;
            p.className = "remove"

            contribuyentes.appendChild(p);

            listaParticipantes.push([nombre.value, parseFloat(monto.value)]);

            montoTotal += parseFloat(monto.value);
            participantes++;

            actualizarResumen(montoTotal, participantes);

            monto.className = "form-control w-50 mb-2";
            nombre.className = "form-control w-50 mb-2";

            monto.value = "";
            monto.setAttribute("placeholder" , "Monto");

            nombre.value = "";
            nombre.setAttribute("placeholder" , "Nombre");

            for(var i = 1; i < contribuyentes.children.length; i++){
                contribuyentes.children[i].addEventListener("click", function(){
                    let nombre = armarNombre(this.textContent);
                    let index = buscarNombre(nombre, listaParticipantes);

                    montoTotal -= listaParticipantes[index][1];
                    participantes--;

                    actualizarResumen(montoTotal, participantes);

                    listaParticipantes.splice(index,1);

                    this.parentNode.removeChild(this);
                });
            }
        }
    };

    boton.addEventListener("click", agregarMonto);
}())

