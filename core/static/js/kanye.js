const URL = "https://api.kanye.rest";

async function LlamarAKanye() {
    const result = await fetch(URL)
    result.json().then(data => {
        const mensaje = data.quote;
        document.getElementById("kanyeTime").innerHTML = `"${mensaje}"`;
    })
}