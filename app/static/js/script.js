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