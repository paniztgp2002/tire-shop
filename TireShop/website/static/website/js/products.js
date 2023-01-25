const categoryDropdown = document.getElementById("category-dropdwon");
const sizesDropdown = document.getElementById("sizes-dropdwon");
const pricesDropdown = document.getElementById("prices-dropdwon");
categoryDropdown.addEventListener('click', () => {
    if (categoryDropdown.classList.contains("animate-down")) {
        categoryDropdown.classList.remove("animate-down");
        categoryDropdown.classList.add("animate-up");
    } else {
        categoryDropdown.classList.remove("animate-up");
        categoryDropdown.classList.add("animate-down");
    }
});
sizesDropdown.addEventListener('click', () => {
    if (sizesDropdown.classList.contains("animate-down")) {
        sizesDropdown.classList.remove("animate-down");
        sizesDropdown.classList.add("animate-up");
    } else {
        sizesDropdown.classList.remove("animate-up");
        sizesDropdown.classList.add("animate-down");
    }
});
pricesDropdown.addEventListener('click', () => {
    if (pricesDropdown.classList.contains("animate-down")) {
        pricesDropdown.classList.remove("animate-down");
        pricesDropdown.classList.add("animate-up");
    } else {
        pricesDropdown.classList.remove("animate-up");
        pricesDropdown.classList.add("animate-down");
    }
});
