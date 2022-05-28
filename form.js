var inputs = document.getElementsByClassName('formulario__input');
for (var i = 0; i < inputs.length; i++) {
    inputs[i].addEventListener('keyup', function(){//evento cuando suelto una tecla, evalua que input este lleno
    if(this.value.length>=1) {
        this.nextElementSibling.classList.add('fijar'); //si tiene al menos un elemento se agrega clase fijar
    } else {
            this.nextElementSibling.classList.remove('fijar');
        }
    });
}
