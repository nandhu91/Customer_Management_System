const API_URL = "/customers";

const idInput = document.getElementById("id");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const phoneInput = document.getElementById("phone");
const cityInput = document.getElementById("city");

const customerForm = document.getElementById("customerForm");
const customerTable = document.getElementById("customerTable");
const statusMsg = document.getElementById("statusMsg");
const submitBtn = document.getElementById("submitBtn");
const cancelBtn = document.getElementById("cancelBtn");

let editMode = false;
let editId = null;

customerForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const customer = {
        id: Number(idInput.value),
        name: nameInput.value,
        email: emailInput.value,
        phone: phoneInput.value,
        city: cityInput.value
    };

    if (editMode) {
        fetch(`${API_URL}/${editId}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(customer)
        }).then(() => {
            showMessage("Customer updated successfully", "green");
            resetForm();
        });
    } else {
        fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(customer)
        }).then(() => {
            showMessage("Customer added successfully", "green");
            resetForm();
        });
    }
});

function loadCustomers() {
    fetch(API_URL)
        .then(res => res.json())
        .then(data => {
            customerTable.innerHTML = "";
            data.forEach(c => {
                customerTable.innerHTML += `
                    <tr>
                        <td>${c.id}</td>
                        <td>${c.name}</td>
                        <td>${c.email}</td>
                        <td>${c.phone}</td>
                        <td>${c.city}</td>
                        <td>
                            <button class="edit" onclick='editCustomer(${JSON.stringify(c)})'>Edit</button>
                            <button class="delete" onclick="deleteCustomer(${c.id})">Delete</button>
                        </td>
                    </tr>
                `;
            });
        });
}

function editCustomer(c) {
    idInput.value = c.id;
    nameInput.value = c.name;
    emailInput.value = c.email;
    phoneInput.value = c.phone;
    cityInput.value = c.city;

    editMode = true;
    editId = c.id;
    submitBtn.textContent = "Update Customer";
    cancelBtn.hidden = false;
}

cancelBtn.addEventListener("click", resetForm);

function deleteCustomer(id) {
    fetch(`${API_URL}/${id}`, { method: "DELETE" })
        .then(() => {
            showMessage("Customer deleted successfully", "red");
            loadCustomers();
        });
}

function resetForm() {
    customerForm.reset();
    editMode = false;
    editId = null;
    submitBtn.textContent = "Add Customer";
    cancelBtn.hidden = true;
    loadCustomers();
}

function showMessage(msg, color) {
    statusMsg.textContent = msg;
    statusMsg.style.color = color;
}

loadCustomers();
