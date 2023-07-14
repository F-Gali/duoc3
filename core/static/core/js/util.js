/*

- FECHA & HORA
- CLIMA + GEOLOCALIZACIÓN
- MAPA
- MODO OSCURO

*/

let clima;
let coordenadasDuocSJ = { latitud:  -33.5000 , longitud: -70.6165 };
let api = "https://api.openweathermap.org/data/2.5/weather?lat=💧&lon=🔥&appid=482487b3d150a9fa227c193f86631615&lang=es";
// El siguiente bool alterna el si mostrar el clima o no (openweather tiene cuotas) 
// y si alternar entre tilemaps bonitos (con cuota) o no.
// En el caso de los mapas hay una alternativa, en el caso de la temperatura, no.
let usarApiConCuota = true;

$(document).ready(()=>{
    // Fecha y Hora
    setInterval( actualizarFechaYHora , 1000 );
    actualizarFechaYHora();

    // Clima & Mapa (Descomentar para el día especial uwu)
    mostrarClima();

    // Modo claro/oscuro
    luminosidad();
})

function actualizarFechaYHora() {
    let ahora = new Date();
    $("#cHora").html( `${ahora.getDate()}/${ahora.getMonth()+1}/${ahora.getFullYear()} 
                <h6 class="cMin">${ahora.getHours()< 10 ? "0" + ahora.getHours() : ahora.getHours()}:${ahora.getMinutes() < 10 ? "0" + ahora.getMinutes() : ahora.getMinutes()}:${ahora.getSeconds() < 10 ? "0" + ahora.getSeconds() : ahora.getSeconds()}</h6>` );
                
}

function mostrarClima(){

    const fracaso = () => _clima(coordenadasDuocSJ.latitud, coordenadasDuocSJ.longitud );  // En caso de rechazar permiso
    const exito = posicion => _clima(posicion.coords.latitude, posicion.coords.longitude);

    function _clima(latitud, longitud){
        if(usarApiConCuota){
            console.log("Mostrando info para coordenadas ("+latitud+" / "+longitud+")");
            $.ajax({ url : api.replace("💧",latitud).replace("🔥",longitud) })
                .done( data => $("#cClima")
                .html( `<img src="${ 'http://openweathermap.org/img/w/'+data.weather[0].icon+'.png'}"/>
                        <div><h6>Clima (${data.name})</h6>
                        <h5>`+data.weather[0].description)+`<h5></div>`);
        }
        
        mostrarMapa(latitud, longitud);
    }
        
    if( navigator.geolocation ) navigator.geolocation.getCurrentPosition( exito, fracaso )
    else fracaso();
}

function mostrarMapa(latitud, longitud){
    let mapa = L.map('MapaPieDePagina').setView( [ latitud, longitud ] , 17 );

    if ( usarApiConCuota ){
        L.tileLayer(`https://tile.jawg.io/527df2f8-2a14-4158-bb87-0959122e486e/{z}/{x}/{y}{r}.png?access-token=J5JPJ5llsdCTIrt9BFWZUTEHhUuvgSWKokA8lqYWjHhe1NnRyk7T1fXF9XIAq77q`, {
            maxZoom: 19}).addTo(mapa);
    }else{
        L.tileLayer(`https://tile.openstreetmap.org/{z}/{x}/{y}.png`, {
            maxZoom: 19}).addTo(mapa);
    }
}

function luminosidad(){
    if( !localStorage.getItem("lumos") ) localStorage.setItem( "lumos", "light" )
    else if( localStorage.getItem("lumos") !== "light") lumos( true );
}

function lumos( forzarOscuro ){
    if(!forzarOscuro)
        localStorage.setItem( "lumos" , localStorage.getItem("lumos") === 'light' ? 'dark' : 'light' );

    $("#cTema").children()[0].innerText = localStorage.getItem("lumos") === 'light' ? "dark_mode" : "light_mode";
    
    let urlClara = document.getElementsByName("tema_claro")[0].getAttribute('content');
    let urlOscura = document.getElementsByName("tema_oscuro")[0].getAttribute('content');

    if(localStorage.getItem("lumos")==='light'){
        $( "link" ).last()[0].href = urlClara;
        $( ".navbar-nav" )[0].children[1].setAttribute( "data-falsebs-theme" , "light" );
        //$( "form" )[0]?.setAttribute( "data-bs-theme" , "light" );
        $("form").toArray().forEach( item=>item.setAttribute( "data-bs-theme" , "light" ));
    }
    else{
        $( "link" ).last()[0].href = urlOscura;
        $( ".navbar-nav" )[0].children[1].setAttribute( "data-bs-theme" , "dark" );
        //$( "form" )[0]?.setAttribute( "data-bs-theme" , "dark" );
        $("form").toArray().forEach( item=>item.setAttribute( "data-bs-theme" , "dark" ));
    }
}


function jutsuReemplazoDeCuerpo(){
    let esLogin = !document.getElementById("loginSection").classList.contains('ocultarSeccion');
    if(esLogin){
        document.getElementById("loginSection").classList.add('ocultarSeccion');
        document.getElementById("registerSection").classList.remove('ocultarSeccion');
    }else{
        document.getElementById("loginSection").classList.remove('ocultarSeccion');
        document.getElementById("registerSection").classList.add('ocultarSeccion');
    }
}