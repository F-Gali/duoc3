let juegos = {};
// Este reemplazo es necesario por razones del DNS del Duoc bloqueando la api
let apiSS = "https://media.rawg.io/media/";
let apiSSProxy = "https://apuc.cl/rawgapi/screenshot/";

document.addEventListener("DOMContentLoaded", ()=>{
    // Buscar todos los <a> con jueguitos
    Array.from(document.getElementsByClassName('g_info')).forEach(atag => {
        let juego = atag.getAttribute('juego');
        if( !juegos.hasOwnProperty(juego) ){
            console.log("CACHEANDO INFO DE " + juego);
            juegos[juego] = undefined;
            guardarInfoJuego(juego);
        }
        atag.addEventListener('click', e => mostrarInfoJuego(juego) );
    });
});

async function guardarInfoJuego(juego){
    const url = "https://apuc.cl/rawgapi/game/"+juego+"/548691206d17468f81dab82819441b90";
    const respuesta = await fetch( url );
    const datos = await respuesta.text();
    juegos[juego] = JSON.parse(datos);

    const urlScreenshots = "https://apuc.cl/rawgapi/search_game/"+juego+"/548691206d17468f81dab82819441b90";
    const respuestaSc = await fetch( urlScreenshots );
    const datosSc = await respuestaSc.text();
    
    if( juego == 'the-legend-of-zelda-breath-of-the-wild-sequel' || juego == 'metroid-prime-remastered')
    {
        juegos[juego].Screen = JSON.parse(datosSc).results[1].short_screenshots;
    }
    else
    {
        juegos[juego].Screen = JSON.parse(datosSc).results[0].short_screenshots;
    }

    }
    

function mostrarInfoJuego(id){
    if ( document.getElementById('infoJuego') ) ocultarInfoJuego();
    let info = document.createElement("div");
    info.id = "infoJuego";
    info.innerHTML = `
        <div class="container py-4">
            <h4>`+juegos[id].name_original+`</h4>
            <p>Lanzado el `+juegos[id].released+`</p>
            <hr>
            <div id="infoCerrar" onclick="ocultarInfoJuego()" >x</div>
            <div class="row">
                <div class="col-md-8">
                    <p style="max-height: 30vh; overflow: auto;"> `+juegos[id].description_raw+`</p>
                </div>
                <div class="col-md-4" >
                    <div id="carouselExampleFade" class="carousel slide carousel-fade" data-bs-ride="carousel">
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                        <img src="`+juegos[id].Screen[0].image.replace(apiSS, apiSSProxy)  +`" class="d-block w-100" alt="...">
                        </div>
                        <div class="carousel-item">
                        <img src="`+juegos[id].Screen[1].image.replace(apiSS, apiSSProxy)+`" class="d-block w-100" alt="...">
                        </div>
                        <div class="carousel-item">
                        <img src="`+juegos[id].Screen[2].image.replace(apiSS, apiSSProxy)+`" class="d-block w-100" alt="...">
                        </div>
                        <div class="carousel-item">
                        <img src="`+juegos[id].Screen[3].image.replace(apiSS, apiSSProxy)+`" class="d-block w-100" alt="...">
                        </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                    </div>
                </div>
            </div>
        </div>`;
    document.getElementsByTagName("main")[0].append( info );
}

const ocultarInfoJuego = () => document.getElementById("infoJuego").remove();