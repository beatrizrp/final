/* Función para determinar el número de jugadores según el número de rondas */

function calculateFighters() {
    var nrounds = document.getElementById('id_numberRounds').value;
    var fighters = Math.pow(2, nrounds);

    document.getElementById('textoJS').innerHTML = "Necesitas " + fighters + " luchadores para este torneo."
}

/* Función que valida todo el formulario */
var ok1 = false;
var ok2 = false;

function validateTournament() {
    validateWeights();
    validateFighters();

    if (ok1 == true && ok2 == true) {
        document.getElementById('crear_torneo').disabled = false;
    } else {
        document.getElementById('crear_torneo').disabled = true;
    }
}

/* Validar que los pesos del torneo suman 100 */

function validateWeights() {
    var f = +document.getElementById('id_strengthWeigth').value;
    var r = +document.getElementById('id_dexterityWeigth').value;
    var d = +document.getElementById('id_resistanceWeigth').value;

    if ((f + r + d) == 100) {
        ok1 = true;   
        document.getElementById('textopesos').innerHTML = "";
    }
    else {
        ok1 = false;
        document.getElementById('textopesos').innerHTML = "Los pesos del torneo tienen que sumar 100.";
    }
}

/* Función para comprobar que el número de luchadores es el especificado */

function validateFighters() {
    var n = document.getElementById('id_numberRounds').value;
    var fg = Math.pow(2, n);
    var fightersSelect = $('#id_fighters option:selected').length;

    console.log(n)
    console.log(fg)
    console.log(fightersSelect)

    if (fg != fightersSelect) {
        document.getElementById('textofg').innerHTML = "Necesitas " + (fg - fightersSelect) + " luchadores más para este torneo."
        ok2 = false;
    } else {
        document.getElementById('textofg').innerHTML = ""
        ok2 = true;
    }
}



