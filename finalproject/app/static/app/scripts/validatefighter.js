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
var ok1 = false;
var ok2 = false;

function validateFighter(){
    validateStats();
    searchUser();

    console.log(ok1);
    console.log(ok2);

    if (ok1 == true && ok2 == true) {
        document.getElementById('btn1').disabled = false;
    }
}

/* Función para validar que las estadisticas no suman más de 10 */

function validateStats() {
    var f = +document.getElementById('id_strength').value;
    var r = +document.getElementById('id_dexterity').value;
    var d = +document.getElementById('id_resistance').value;

    if ((f + r + d) == 10) {
        ok1 = true;
    }
}

/* Unir login y usuario*/

function searchUser() {
    user = document.getElementById('hiuser').innerText;
    console.log(user);
    a = user.lenght
    console.log(a)
    userSplit = user.split(5, a);

    console.log(userSplit)

    if (userSplit != null) {
        document.getElementById('nouser').innerHTML = "Necesitas un usuario para loguearte";
    } else {
        ok2 = true;
    }
}