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