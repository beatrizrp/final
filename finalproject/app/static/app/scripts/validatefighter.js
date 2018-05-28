/* Función para generar nombre aleatorio */
const rname = document.getElementById('id_alias')
const url = 'https://swapi.co/api/people/';

function getRandomName() {
    var request = new XMLHttpRequest();
    var rnumber = Math.floor((Math.random() * 100) + 1);
    
    request.open('GET', url + rnumber, true);

    request.onload = function () {
        // JSON data 
        var data = JSON.parse(this.response);
        if (request.status >= 200 && request.status < 400) {
            rname.value = data.name;
            console.log(rname)
        } else {
            console.log('error');
        }
    }
    
request.send();
}


/* Función para validar que las estadisticas no suman más de 10 */

function validateStats() {
    var f = +document.getElementById('id_strength').value;
    var r = +document.getElementById('id_dexterity').value;
    var d = +document.getElementById('id_resistance').value;

    if ((f + r + d) == 10) {
        document.getElementById('btn1').disabled = false;
    } else {
        document.getElementById('btn1').disabled = true;
    }
}
