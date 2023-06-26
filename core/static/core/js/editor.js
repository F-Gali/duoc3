$(document).ready(()=>{
  let xx = document.getElementById("test");
})

function setBold(){
    document.execCommand('bold');
}
function formato(tipo){
    switch(tipo){
        case "bold" : document.execCommand('bold'); break;
        case "italic" : document.execCommand('italic'); break;
        case "strikeThrough" : document.execCommand('strikeThrough'); break;
        case "underline" : document.execCommand('underline'); break;
        case "lorem" : document.execCommand('insertText',false,`Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas condimentum finibus pharetra. Ut dapibus dolor nec dictum ultrices. Fusce mattis odio id eros interdum, ut finibus nisi sodales. Quisque ullamcorper felis consequat orci varius commodo. Aliquam tempus, tortor ac tincidunt suscipit, lorem ex euismod justo, sed faucibus sapien tortor in purus. Donec vehicula a felis non laoreet. Quisque cursus tortor velit. `); break;
    }
}
function validarEditior(){
    document.getElementById("id_html_body").value = document.getElementById("areaedit").innerHTML;
    document.getElementById("articulonuevo").submit();
}

function validarComentario(){
    document.getElementById("id_mensaje").value = document.getElementById("areaedit").innerHTML;
    document.getElementById("comentarionuevo").submit();
}