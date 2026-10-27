
const grid = document.getElementById("productGrid");
const cards = [...document.querySelectorAll(".product-card")];

const searchInput = document.getElementById("searchInput");
const priceFilter = document.getElementById("priceFilter");
const maxPriceLabel = document.getElementById("maxPriceLabel");
const stockFilter = document.getElementById("stockFilter");
const sortSelect = document.getElementById("sortSelect");
const resultsCount = document.getElementById("resultsCount");
const emptyMessage = document.getElementById("emptyMessage");
const cartCount = document.getElementById("cartCount");

let activeCategory = "Всі фрукти";
let cartItems = 0;

function applyFilters() {
    const search = searchInput.value.trim().toLocaleLowerCase("uk");
    const maxPrice = Number(priceFilter.value);

    maxPriceLabel.textContent = `${maxPrice} грн`;

    let visibleCards = cards.filter(card => {
        const matchesSearch = card.dataset.name.includes(search);
        const matchesCategory =
            activeCategory === "Всі фрукти" ||
            card.dataset.category === activeCategory;
        const matchesPrice = Number(card.dataset.price) <= maxPrice;
        const matchesStock =
            !stockFilter.checked || card.dataset.stock === "true";

        return matchesSearch && matchesCategory &&
               matchesPrice && matchesStock;
    });

    switch (sortSelect.value) {
        case "price-asc":
            visibleCards.sort((a, b) =>
                Number(a.dataset.price) - Number(b.dataset.price));
            break;
        case "price-desc":
            visibleCards.sort((a, b) =>
                Number(b.dataset.price) - Number(a.dataset.price));
            break;
        case "rating":
            visibleCards.sort((a, b) =>
                Number(b.dataset.rating) - Number(a.dataset.rating));
            break;
        case "name":
            visibleCards.sort((a, b) =>
                a.dataset.name.localeCompare(b.dataset.name, "uk"));
            break;
    }

    cards.forEach(card => {
        card.hidden = !visibleCards.includes(card);
    });

    visibleCards.forEach(card => grid.appendChild(card));

    resultsCount.textContent = `Знайдено ${visibleCards.length} товарів`;
    emptyMessage.hidden = visibleCards.length !== 0;
}

document.querySelectorAll(".category-button").forEach(button => {
    button.addEventListener("click", () => {
        activeCategory = button.dataset.category;

        document.querySelectorAll(".category-button").forEach(item => {
            item.classList.toggle("selected", item === button);
        });

        applyFilters();
    });
});

searchInput.addEventListener("input", applyFilters);
priceFilter.addEventListener("input", applyFilters);
stockFilter.addEventListener("change", applyFilters);
sortSelect.addEventListener("change", applyFilters);

document.getElementById("gridView").addEventListener("click", () => {
    grid.classList.remove("list-view");
    document.getElementById("gridView").classList.add("selected");
    document.getElementById("listView").classList.remove("selected");
});

document.getElementById("listView").addEventListener("click", () => {
    grid.classList.add("list-view");
    document.getElementById("listView").classList.add("selected");
    document.getElementById("gridView").classList.remove("selected");
});

document.querySelectorAll("[data-add]").forEach(button => {
    button.addEventListener("click", () => {
        cartItems += 1;
        cartCount.textContent = cartItems;

        const originalText = button.textContent;
        button.textContent = "✓ Додано";
        button.disabled = true;

        setTimeout(() => {
            button.textContent = originalText;
            button.disabled = false;
        }, 900);
    });
});

applyFilters();
