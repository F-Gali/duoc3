$(document).ready(()=>{

    const genero = { 0:'No especificado' , 1: 'Hombre' , 2: 'mujer'};
    const carrera = { 1: 'Analista Programador', 2: 'Ingeniería Informática' , 3: 'Ingeniero en Conectividad y Redes'}

    if( !localStorage.getItem("contacto") ){
        $("#contMensajes").html(`<div class="itemContacto"><h6>No hay items</h6></div>`);
    }else{
        let items = JSON.parse( localStorage.getItem("contacto") );
        if(items.entradas.length == 0){
            $("#contMensajes").html(`<div class="itemContacto"><h6>No hay items</h6></div>`);
        }else{
            console.log("test");
            let _html = ``;

            // NOTA: Este formulario entero es vulnerable a XSS dado que es posible insertar html/js. 
            // La forma correcta sería encodear todos los caracteres reservados a HTML Entities.
            // Dicho eso, es una tarea así que who cares

            items.entradas.map(item => _html += `
                <div class="itemContacto">
                    <div class="perfil">
                        <h5>
                            <span class="profilep material-symbols-outlined">account_circle</span>${item.nombre + " " + item.apellido}
                        <h5>    
                    </div>
                    <div class="infodesc">
                        <div class="infocampo">
                            <h6>RUT</h6>
                            <span>${ item.rut }</span>
                        </div>
                        <div class="infocampo">
                            <h6>EMAIL</h6>
                            <span>${ item.email }</span>
                        </div>
                        <div class="infocampo">
                            <h6>GÉNERO</h6>
                            <span>${ genero[item.genero] }</span>
                        </div>
                        <div class="infocampo">
                            <h6>NÚMERO</h6>
                            <span>${ item.numero }</span>
                        </div>
                        <div class="infocampo">
                            <h6>CARRERA</h6>
                            <span>${ carrera[item.carrera] }</span>
                        </div>
                    </div>
                    <div class="infomensaje">
                        <b>Dice: </b>${item.mensaje}
                    </div>
                </div>`
            );
            $("#contMensajes").html(_html);
        }
    }
})