const container = document.getElementById('formulario')
    ocultar = document.querySelectorAll('.showHidePw'),
    campos = document.querySelectorAll('.password');

// CODIGO PARA OCULTAR

ocultar.forEach(eyeIcon =>{
    eyeIcon.addEventListener('click', ()=> {
        campos.forEach (campos =>{
            if(campos.type=== 'password'){
                campos.type = 'text' ;
            }else{
                campos.type = 'password';
           
            }
        })
    })

})

// // FUNCION ANTERIOR QUE CAPTURA LOS DATOS DEL FORM

// function capturar(){

//     function user(usuario,contraseña){
//         this.usuario=usuario;
//         this.password=password;
//     }
//     var nombyape=document.getElementById ('usuario').value;
//     var pass=document.getElementById ('password').value;
    
//     nuevoUsuario= new user(nombyape,pass);
//     console.log(nuevoUsuario)

//     if (nombyape=='') {
//         alert('El usuario es obligatorio')
//     }
    
//     if (pass=='') {
//         alert('La contraseña es obligatoria')
//     }

//     console.log('La Usuario es:' + nombyape);
//     console.log('La contraseña es:' + pass);
//     agregar();
// }


// //array para guardar los nuevos usuarios

// var baseDatos = [];
// function agregar (){
//     baseDatos.push(nuevoUsuario);
//     console.log (baseDatos)
// }

