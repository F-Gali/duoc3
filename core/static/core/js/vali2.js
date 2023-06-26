$("#error_rut")[0].style.display="none";
$("#error_rut_min")[0].style.display="none";
$("#error_nombre_min")[0].style.display="none";
$("#error_nombre_max")[0].style.display="none";
$("#error_nombre_invalido")[0].style.display = "none";
$("#error_apellido_invalido")[0].style.display="none";
$("#error_apellido_min")[0].style.display="none";
$("#error_apellido_max")[0].style.display="none";
$("#error_email")[0].style.display="none";
$("#error_email_min")[0].style.display="none";
$("#error_password")[0].style.display="none";
$("#error_nacimiento")[0].style.display="none";
$("#error_genero")[0].style.display="none";
$("#error_numero")[0].style.display="none";
$("#error_numero_min")[0].style.display="none";
$("#error_carrera")[0].style.display="none";
$("#error_validarT")[0].style.display="none";
//Validar Rut
function validarRut(){
let rut = $("#rut")[0].value;
if(rut.trim().length == 0){
    $("#error_rut_min")[0].style.display = "inline";
    $("#rut")[0].classList.remove("is-invalid");
}
rut = rut.replace(/[.-]/g, '');
if (rut.length == 9) {
var body = rut.slice(0, -1); // Extract the body (all digits except the verification digit)
var dv = rut.slice(-1).toUpperCase(); // Extract the verification digit
var rutSum = 0;
var multiplier = 2;
for (var i = body.length - 1; i >= 0; i--) {
    rutSum += parseInt(body.charAt(i)) * multiplier;
    multiplier = multiplier === 7 ? 2 : multiplier + 1;
}
var expectedDV = 11 - (rutSum % 11);
expectedDV = expectedDV === 11 ? 0 : expectedDV === 10 ? 'K' : expectedDV.toString();
if(dv !== expectedDV){
    $("#error_rut")[0].style.display = "inline";
    $("#rut")[0].classList.add("is-invalid");

} 
if(dv == expectedDV){
    $("#error_rut")[0].style.display = "none";
    $("#error_rut_min")[0].style.display = "none";
    $("#rut")[0].classList.remove("is-invalid");
    $("#rut")[0].classList.add("is-valid");
}}
}

//Validar Nombre
function validarNombre(){
    let nombre = $("#nombre")[0].value;
    $("#error_nombre_invalido")[0].style.display = "none";
    $("#error_nombre_min")[0].style.display = "none";
    $("#error_nombre_max")[0].style.display = "none";
    $("#nombre")[0].classList.remove("is-invalid");
    $("#nombre")[0].classList.add("is-valid");
    let rgNombre = /^[a-zA-Z]+$/;
    if (nombre.trim().length == 0){
        $("#error_nombre_invalido")[0].style.display = "none";
        $("#error_nombre_min")[0].style.display = "inline";
        $("#error_nombre_max")[0].style.display = "none";
        $("#nombre")[0].classList.add("is-invalid");
        return false;
    }
    if (rgNombre.test(nombre) == false){
        $("#error_nombre_invalido")[0].style.display = "inline";
        $("#error_nombre_min")[0].style.display = "none";
        $("#error_nombre_max")[0].style.display = "none";
        $("#nombre")[0].classList.add("is-invalid");
        return false;
    }
    if(nombre.trim().length > 30){
        $("#error_nombre_invalido")[0].style.display = "none";
        $("#error_nombre_max")[0].style.display = "inline";
        $("#error_nombre_min")[0].style.display = "none";
        $("#nombre")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

//Validar Apellido
function validarApellido(){
    let apellido = $("#apellido")[0].value;
    $("#error_apellido_invalido")[0].style.display = "none";
    $("#error_apellido_min")[0].style.display = "none";
    $("#error_apellido_max")[0].style.display = "none";
    $("#apellido")[0].classList.remove("is-invalid");
    $("#apellido")[0].classList.add("is-valid");
    let rgApellido = /^[a-zA-Z]+$/;
    if (apellido.trim().length == 0){
        $("#error_apellido_invalido")[0].style.display = "none";
        $("#error_apellido_min")[0].style.display = "inline";
        $("#error_apellido_max")[0].style.display = "none";
        $("#apellido")[0].classList.add("is-invalid");
        return false;
    }
    if (rgApellido.test(apellido) == false){
        $("#error_apellido_invalido")[0].style.display = "inline";
        $("#error_apellido_min")[0].style.display = "none";
        $("#error_apellido_max")[0].style.display = "none";
        $("#apellido")[0].classList.add("is-invalid");
        return false;
    }
    if(apellido.trim().length > 30){
        $("#error_apellido_invalido")[0].style.display = "none";
        $("#error_apellido_max")[0].style.display = "inline";
        $("#error_apellido_min")[0].style.display = "none";
        $("#apellido")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

//Validar Email
function validarEmail(){
    let email = $("#email")[0].value;
    $("#error_email")[0].style.display = "none";
    $("#error_email_min")[0].style.display = "none";
    $("#email")[0].classList.remove("is-invalid");
    $("#email")[0].classList.add("is-valid");
    let rgEmail = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
    if (email.trim().length == 0){
        $("#error_email")[0].style.display = "none";
        $("#error_email_min")[0].style.display = "inline";
        $("#email")[0].classList.add("is-invalid");
        return false;
    }
    if (rgEmail.test(email) == false){  
        $("#error_email_min")[0].style.display = "none";
        $("#error_email")[0].style.display = "inline";
        $("#email")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

//Validar Password
function validarPassword(){
    let password = $("#password")[0].value;
    let rgPass = /^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{6,10}$/;
    if(rgPass.test(password) == false){
        $("#error_password")[0].style.display = "inline";
        $("#password")[0].classList.add("is-invalid");
        return false;
    }
    else{
        $("#error_password")[0].style.display = "none";
        $("#password")[0].classList.remove("is-invalid");
        $("#password")[0].classList.add("is-valid");
        return true;
    }
}

//Validar Fecha de Nacimiento
function validarFecha(){
    $("#error_nacimiento")[0].style.display = "none";
    $("#fecha_nazi")[0].classList.remove("is-invalid");
    let fecha_nazi = $("#fecha_nazi")[0].value;
    if((new Date(fecha_nazi)) > (new Date())){
        $("#error_nacimiento")[0].style.display = "inline";
        $("#fecha_nazi")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

//Validar Mensaje
const mensajeInput = document.getElementById('mensaje');
const cont_carac = document.getElementById('cont_carac');
const max_carac = 100;


// Add event listener to the input element
mensaje.addEventListener('input', function() {
    const mensaje = mensajeInput.value;
    const mensajeLength = mensaje.length;

    cont_carac.textContent = max_carac - mensajeLength;
    if (mensajeLength> max_carac){
        mensajeInput.value = mensaje.slice(0, max_carac);
    }
});

//Validar Genero
let generoSeleccionado = -1;
function validarGenero(){
    $("#error_genero")[0].style.display = "none";

    let elegido = -1;
    $("input").map( (i, item) => {
        item.getAttribute("name") == "genero" ? (item.checked ? elegido = item.value : null ) : null
    });

    if(elegido == -1){
        $("#error_genero")[0].style.display = "inline";
        return false;
    }
    generoSeleccionado = elegido;
    return true;
}

//validar Numero
function validarNumero(){
    let numero = $("#numero")[0].value;
    $("#error_numero")[0].style.display = "none";
    $("#error_numero_min")[0].style.display = "none";
    let rgNumero = /^(?:\+?56|0)(9\d{8})$/;
    if(numero.trim().length == 0){
        $("#error_numero")[0].style.display = "none";
        $("#error_numero_min")[0].style.display = "inline";
        $("#numero")[0].classList.add("is-invalid");
        return false;
    }
    else if(rgNumero.test(numero) == false){
        $("#error_numero_min")[0].style.display = "none";
        $("#error_numero")[0].style.display = "inline";
        $("#numero")[0].classList.add("is-invalid");
        return false;
    }
    else{
        $("#error_numero")[0].style.display = "none";
        $("#error_numero_min")[0].style.display = "none";
        $("#numero")[0].classList.remove("is-invalid");
        $("#numero")[0].classList.add("is-valid");
        return true;
    }
}

//Validacion CARRERA
function validarCarrera(){
    if(carrera == null){
        document.getElementById("error_carrera").style.display = "inline";
        document.getElementById("carrera").classList.add("is-invalid");
        return false;
    }
    else{
        document.getElementById("error_carrera").style.display = "none";
        document.getElementById("carrera").classList.remove("is-invalid");
        document.getElementById("carrera").classList.add("is-valid");
        return true;
    }
}

//Submit
function validarT(){
    if(!validarNombre()) return;
    if(!validarApellido()) return;
    if(!validarEmail()) return;
    if(!validarPassword()) return;
    if(!validarFecha()) return;
    if(!validarGenero()) return;
    if(!validarNumero()) return;
    if(!validarCarrera()) return;


    // localStorage.removeItem("contacto")
    // ^ Línea útil para debuggear

    if( !localStorage.getItem( "contacto" ) ){
        localStorage.setItem( "contacto" , JSON.stringify( { entradas : [] } ) );
    }
    let listaDatos = JSON.parse( localStorage.getItem( "contacto" ) );
    listaDatos.entradas.push({
        nombre : $("#nombre")[0].value,
        apellido : $("#apellido")[0].value,
        password : $("#password")[0].value,
        rut : $("#rut")[0].value,
        email : $("#email")[0].value,
        fechaNazi : $("#fecha_nazi")[0].value,
        mensaje : $("#mensaje")[0].value,
        genero : generoSeleccionado,
        numero : $("#numero")[0].value,
        carrera : $("#carrera")[0].value,
    });
    console.log(listaDatos);
    localStorage.setItem( "contacto", JSON.stringify(listaDatos) );
    
    $("form").html("<h6>Tu mensaje se ha enviado con éxito.</h6>")
}

function validarMensaje(){
    if(!validarNombre()) return;
    if(!validarApellido()) return;
    if(!validarEmail()) return;
    document.getElementById("mensajenuevo").submit();
}

