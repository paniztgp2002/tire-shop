const inc = document.getElementsByClassName("input-number-increment")[0];
const dec = document.getElementsByClassName("input-number-decrement")[0];
const intinp = document.getElementsByClassName("input-number")[0]

inc.addEventListener('click', () => {
    if ((parseInt(intinp.value) + 10000 <= intinp.max) && (parseInt(intinp.value) + 10000 >= intinp.min)) {
        intinp.value = parseInt(intinp.value) + 10000;
    }
});

dec.addEventListener('click', () => {
    if ((parseInt(intinp.value) - 10000 <= intinp.max) && (parseInt(intinp.value) - 10000 >= intinp.min)) {
        intinp.value = parseInt(intinp.value) - 10000;
    }
});
