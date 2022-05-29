
// Funcion que captura los datos del form

function capturar(){

    function user(usuario,contraseña){
        this.usuario=usuario;
        this.password=password;
    }
    var nombyape=document.getElementById ('usuario').value;
    var pass=document.getElementById ('password').value;
    
    nuevoUsuario= new user(nombyape,pass);
    console.log(nuevoUsuario)

    if (nombyape=='') {
        alert('El usuario es obligatorio')
    }
    
    if (pass=='') {
        alert('La contraseña es obligatoria')
    }

    console.log('La Usuario es:' + nombyape);
    console.log('La contraseña es:' + pass);
    agregar();
}


//array para guardar los nuevos usuarios

var baseDatos = [];
function agregar (){
    baseDatos.push(nuevoUsuario);
    console.log (baseDatos)
}

