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


const apply = document.getElementById("apply");
const cancel = document.getElementById("cancel");
const sizeFrom = document.getElementById("size-from");
const sizeTill = document.getElementById("size-till");
const priceFrom = document.getElementById("price-from");
const priceTill = document.getElementById("price-till");
const cbTire = document.getElementById("cbTire");
const cbTube = document.getElementById("cbTube");
const cbRim = document.getElementById("cbRim");
const collapseTypes = document.getElementById("collapse-types");
const collapseSizes = document.getElementById("collapse-sizes");
const collapsePrices = document.getElementById("collapse-prices");

url = new URL(location.href);
if (url.searchParams.getAll("type").includes("tire")) {
    cbTire.checked = true;
    collapseTypes.classList.add("show");
}
if (url.searchParams.getAll("type").includes("tube")) {
    cbTube.checked = true;
    collapseTypes.classList.add("show");
}
if (url.searchParams.getAll("type").includes("rim")) {
    cbRim.checked = true;
    collapseTypes.classList.add("show");
}

if (url.searchParams.get("sizeFrom") && url.searchParams.get("sizeTill")) {
    sizeFrom.value = parseInt(url.searchParams.get("sizeFrom"))
    sizeTill.value = parseInt(url.searchParams.get("sizeTill"))
    collapseSizes.classList.add("show");
}
if (url.searchParams.get("priceFrom") && url.searchParams.get("priceTill")) {
    priceFrom.value = parseInt(url.searchParams.get("priceFrom"))
    priceTill.value = parseInt(url.searchParams.get("priceTill"))
    collapsePrices.classList.add("show");
}

cbTire.addEventListener('input', e => {
    url.searchParams.append('type', 'tire');
});

cbTube.addEventListener('input', e => {
    url.searchParams.append('type', 'tube');
});

cbRim.addEventListener('input', e => {
    url.searchParams.append('type', 'rim');
});

sizeFrom.addEventListener('input', e => {
    url.searchParams.delete('sizeFrom');
    url.searchParams.append('sizeFrom', sizeFrom.value);
});

sizeTill.addEventListener('input', e => {
    url.searchParams.delete('sizeTill');
    url.searchParams.append('sizeTill', sizeTill.value);
});

priceFrom.addEventListener('input', e => {
    url.searchParams.delete('priceFrom');
    url.searchParams.append('priceFrom', priceFrom.value);
});

priceTill.addEventListener('input', e => {
    url.searchParams.delete('priceTill');
    url.searchParams.append('priceTill', priceTill.value);
});

apply.addEventListener('click', e => {
    window.location.href = url;
});

cancel.addEventListener('click', e => {
    for (const [key, value] of url.searchParams.entries()) {
        url.searchParams.delete(key);
    }
    url.searchParams.forEach((value, key) => {
        url.searchParams.delete(key);
      });
    window.location.href = url;
});

[].forEach.call(document.getElementsByClassName("filter"), filter => {
    filter.addEventListener('click', e => {
        if (e.currentTarget.dataset.filter == "size") {
            url.searchParams.delete("sizeFrom");
            url.searchParams.delete("sizeTill");
        }
        if (e.currentTarget.dataset.filter == "price") {
            url.searchParams.delete("priceFrom");
            url.searchParams.delete("priceTill");
        }
        url.searchParams.delete(e.currentTarget.dataset.filter);
        window.location.href = url;
    });
});
