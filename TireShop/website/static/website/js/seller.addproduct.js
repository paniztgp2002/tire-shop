const type = document.getElementById('type');
const pattern = document.getElementById('id_pattern');
pattern.required = true;

type.addEventListener('input', e => {
    if (type.value != 'tire') {
        pattern.parentElement.parentElement.style.visibility = "hidden";
        pattern.required = false;

    } else {
        pattern.parentElement.parentElement.style.visibility = "visible";
        pattern.required = true;
    }
});
