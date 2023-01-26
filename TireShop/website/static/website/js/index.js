const navbar = document.getElementsByClassName("navbar")[0];
const navBorder = document.getElementById("navborder");

const debounce = (fn) => {
    let frame;
    return (...params) => {
        if (frame) {
            cancelAnimationFrame(frame);
        }
        frame = requestAnimationFrame(() => {
            fn(...params);
        });
    }
};

const storeScroll = () => {
    let y = window.scrollY;
    if (y > 567) {
        navbar.style.backgroundColor = "rgba(53, 51, 64, 1)";
        navBorder.style.background = "linear-gradient(to right,  rgba(105, 105, 105, 0) 0%,rgba(210, 210, 210, 0) 50%,rgba(105, 105, 105, 0) 100%)";
    } else {
        navbar.style.backgroundColor = `rgba(53, 51, 64, ${y / 567})`;
        navBorder.style.background = `linear-gradient(to right,  rgba(105, 105, 105, 0) 0%,rgba(210, 210, 210, ${1 - (y / 567)}) 50%,rgba(105, 105, 105, 0) 100%)`;
    }
}

document.addEventListener('scroll', debounce(storeScroll), { passive: true });
storeScroll();


var selectedGroup = "all";
const all = document.getElementById("all-btn");
const tires = document.getElementById("tires-btn");
const tubes = document.getElementById("tubes-btn");
const rims = document.getElementById("rims-btn");

btnGroup = { all: all, tires: tires, tubes: tubes, rims: rims };

function selectGroupFunc(selection) {
    selectedGroup = selection;
    btnGroup[selection].style.backgroundColor = "#5BC8C5";
    Object.keys(btnGroup).forEach(element => {
        if (element != selection) {
            btnGroup[element].style.backgroundColor = "#414141";
        }
    });
}

const searchSubmit = document.getElementById("search-submit");
const searchForm = document.getElementById("search-form");
searchSubmit.addEventListener('click', () => {
    searchForm.elements['type'].value = selectedGroup;
    if (searchForm.elements['name'].value) {
        searchForm.submit();
    }
});

new Splide('.splide', {
    type: 'loop',
    perPage: 4,
    speed: 600,
    perMove: 1,
    pagination: false,
}).mount();
