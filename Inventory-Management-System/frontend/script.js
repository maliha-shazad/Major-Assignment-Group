let products = [];
let editId = null;

// DOM Elements
const productForm = document.getElementById('productForm');
const productIdInput = document.getElementById('productId');
const productNameInput = document.getElementById('productName');
const productQuantityInput = document.getElementById('productQuantity');
const productPriceInput = document.getElementById('productPrice');
const productTableBody = document.querySelector('#productTable tbody');
const cancelUpdateBtn = document.getElementById('cancelUpdate');

// Add or Update Product
productForm.addEventListener('submit', function(e) {
    e.preventDefault();

    const name = productNameInput.value;
    const quantity = parseInt(productQuantityInput.value);
    const price = parseFloat(productPriceInput.value);

    if (editId === null) {
        // Add Product
        const product = {
            id: products.length + 1,
            name,
            quantity,
            price
        };
        products.push(product);
    } else {
        // Update Product
        const product = products.find(p => p.id === editId);
        product.name = name;
        product.quantity = quantity;
        product.price = price;
        editId = null;
        cancelUpdateBtn.style.display = 'none';
        productForm.querySelector('button[type="submit"]').textContent = 'Add Product';
    }

    productForm.reset();
    renderTable();
});

// Render Products Table
function renderTable() {
    productTableBody.innerHTML = '';
    products.forEach(product => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${product.id}</td>
            <td>${product.name}</td>
            <td>${product.quantity}</td>
            <td>${product.price}</td>
            <td>
                <button class="edit" onclick="editProduct(${product.id})">Edit</button>
                <button class="delete" onclick="deleteProduct(${product.id})">Delete</button>
            </td>
        `;
        productTableBody.appendChild(row);
    });
}

// Edit Product
function editProduct(id) {
    const product = products.find(p => p.id === id);
    productNameInput.value = product.name;
    productQuantityInput.value = product.quantity;
    productPriceInput.value = product.price;
    editId = id;
    cancelUpdateBtn.style.display = 'inline';
    productForm.querySelector('button[type="submit"]').textContent = 'Update Product';
}

// Cancel Update
cancelUpdateBtn.addEventListener('click', () => {
    productForm.reset();
    editId = null;
    cancelUpdateBtn.style.display = 'none';
    productForm.querySelector('button[type="submit"]').textContent = 'Add Product';
});

// Delete Product
function deleteProduct(id) {
    products = products.filter(p => p.id !== id);
    renderTable();
}

// Initial Render
renderTable();
