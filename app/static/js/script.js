//agrega evento de click y tambien navegacion a los nav-item
document.querySelectorAll('nav-item').forEach(item => {
    item.addEventListener('click', event => {
        const link = item.getAttribute('href');
        window.location.href = link;
    });
});

function tipoDocumento() {
    
    var select = document.getElementById('select-documento');
    var value = select.options[select.selectedIndex].value;
    
    var title = document.getElementById('option-title');
    var message = document.getElementById('option-message').firstElementChild;

    switch (value) {
        case "0":
            title.innerText = "RUT del Paciente";
            message.textContent = "RUT";
            break;
        case "1":
            title.innerText = "Número de Pasaporte del Paciente";
            message.textContent = "Número de Pasaporte";
            break;
    
        default:
            title.innerText = "RUT del Paciente";
            message.textContent = "RUT";
            break;
    }
}

// controla los checkbox para que tambien se puedan activar clickeando el parent
document.querySelectorAll('.evaluacion-item').forEach(item => {
    item.addEventListener('click', event => {
        if (!item.getElementsByTagName('input').item(0).matches(':hover')) {
            item.getElementsByTagName('input').item(0).checked = !item.getElementsByTagName('input').item(0).checked;
        }
        if (document.URL.indexOf("/pre-quirurgica/evaluacion/evaluacion-riesgo") >= 0) {
            riesgoCalculator();
        }
    });
});

function riesgoCalculator() {
    const output = document.getElementById('riesgo-output');

    let items = document.querySelectorAll('.evaluacion-item');
    
    var riesgo = 0;


    for (let index = 0; index < items.length; index++) {

        // verifica si el elemento actual esta checked y si el riesgo de ese elemento es mayor que el riesgo almacenado
        if (items.item(index).getElementsByTagName('input').item(0).checked
            && Number.parseInt(items.item(index).dataset.riesgo) > riesgo)
        {
            riesgo = Number.parseInt(items.item(index).dataset.riesgo);
        }
        
    }

    switch (riesgo) {
        case 1:
            output.textContent = 'MEDIO';
            break;
        case 2:
            output.textContent = 'ALTO';

            break;
    
        default:
            output.textContent = 'BAJO';
            break;
    }
    
}


//CONTROLA EL STEPS PROGRESS BAR
if(document.URL.indexOf("pre-quirurgica/evaluacion/") >= 0 && document.URL.indexOf("pre-quirurgica/evaluacion/buscar-interconsulta") == -1){ 
    
    var data = document.getElementById('parent-steps').dataset.step;
    let steps = document.getElementsByClassName('step');

    for (let index = 0; index < steps.length; index++) {
        const element = steps[index];
        if (index == data) {
            element.classList.add('activo');
            break;
        }

        if(index < data){
            element.classList.add('listo');
            element.getElementsByClassName('circle')[0].textContent = '🗸';
        }
        
    }
}

if (document.URL.indexOf("pre-quirurgica/evaluacion/derivacion") >= 0) {
    console.log('awa')
    changeWeek(0);

    document.querySelectorAll('.agendar-button').forEach(item => {
        item.addEventListener('click', event =>{
            if (!item.classList.contains('activo')){
                changeItem(item, 'agendar-button', false);
            }
        });
    });
}

function changeWeek(option) {
    if (!localStorage.getItem('delta')) {
        localStorage.setItem('delta', '0');
    }
    const delta = Number.parseInt(localStorage.getItem('delta')) + option;
    localStorage.setItem('delta', delta.toString());
                
    let day = new Date();
    const weekday = day.getDay();

    day.setDate(day.getDate() - weekday);
    day.setDate(day.getDate() + (delta*7));
    
    // console.clear();
    // console.log(day.toDateString());

    let dates = [];

    for (let index = 0; index < 7; index++) {
        day.setDate(day.getDate() + 1);
        // console.log(day.toDateString());
        dates.push([day.toLocaleString('default', { month: "short"}), String(day.getDate()).padStart(2, '0')]);
    }

    let mesButton = document.getElementsByClassName('agendar-mes');

    for (let index = 0; index < 6; index++) {
        mesButton.item(index).innerHTML =  dates[index][0].substring(0, 3);
    }

    let diaButton = document.getElementsByClassName('button-dia');
    for (let index = 0; index < 6; index++) {
        diaButton.item(index).innerHTML =  dates[index][1] ;
    }
    
}

function changeItem(element = Node, className = String, multiple = Boolean) {
    if (!multiple) {
        let buttons = document.getElementsByClassName(className);
        
        for (let index = 0; index < buttons.length; index++) {
            if (buttons.item(index).classList.contains('activo')) {
                buttons.item(index).classList.remove('activo');
            }
        }
    }
    if (element.classList.contains('activo')) {
        element.classList.remove('activo');
    }else{
        element.classList.add('activo');
    }
}
