const form = document.getElementById("form");
const userType = document.getElementById("id_user_type");
const customerSubmit = document.getElementById("customer");
const sellerSubmit = document.getElementById("seller");

customerSubmit.addEventListener('click', () => {
    userType.value = "customer";
    form.elements.array.forEach(element => {
        if (!element.value) {
            return;
        }
    });
    form.submit();
});

sellerSubmit.addEventListener('click', () => {
    userType.value = "seller";
    form.elements.array.forEach(element => {
        if (!element.value) {
            return;
        }
    });
    form.submit();
});
