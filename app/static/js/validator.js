function rutInput(element = Node){
    element.value = format(element.value);
}

function format(rut) {

    const current = rut.replace(/^0+/, "");

    if (current != '' && current.length > 1) {

        const unformatRut = this.unformat(current);
        const cleanRut = unformatRut.substring(0, unformatRut.length - 1);

        // let rutNumberFormat = new Intl.NumberFormat('de-DE').format(cleanRut)

        let rutNumberFormat = "";

        let i = 0;
        let j = 1;

        for (i = cleanRut.length - 1; i >= 0; i--) {
            rutNumberFormat = cleanRut.charAt(i) + rutNumberFormat;
            if (j % 3 == 0 && j <= cleanRut.length - 1) {
                rutNumberFormat = "." + rutNumberFormat;
            }
            j++;
        }

        let dv = unformatRut.substring(unformatRut.length - 1);
        rutNumberFormat = rutNumberFormat + "-" + dv;
        return rutNumberFormat;
    }
    return current;
}


function unformat(rut) {
    return rut.replace(/\./g, "").replace(/-/g, "");
}
