function changeOption() {
    let selectBox = document.getElementById("cipher");
    let selectedValue = selectBox.options[selectBox.selectedIndex].value;
    let form_key = document.getElementById("form_key");
    let form_key_doicho = document.getElementById("form_key_doicho");
    let form_key_thaythedon = document.getElementById("form_key_thaythedon");
    let form_key_vigenere = document.getElementById("form_key_vigenere");
    let form_key_RSA = document.getElementById("form_key_RSA");
    //    Key ceasar
    if (selectedValue == 1) {
        form_key.classList.remove("d-none");
    } else {
        form_key.classList.add("d-none");
    }
    //    key doi cho
    if (selectedValue == 2) {
        form_key_doicho.classList.remove("d-none");
    } else {
        form_key_doicho.classList.add("d-none");
    }
    //    key thay thế
    if (selectedValue == 3) {
        form_key_thaythedon.classList.remove("d-none");
    } else {
        form_key_thaythedon.classList.add("d-none");
    }
    //    key vigenere
    if (selectedValue == 5 || selectedValue == 6) {
        form_key_vigenere.classList.remove("d-none");
    } else {
        form_key_vigenere.classList.add("d-none");
    }
    //    key form_key_RSA
    if (selectedValue == 8) {
        let form = document.getElementById('contact-form').submit();

    }
}

function createKey(){
    let input = document.getElementById('input_key');
    input.value = 0;
    console.log(input.value)
    let form = document.getElementById('contact-form').submit();
}