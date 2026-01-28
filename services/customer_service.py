import json
from models.customer_model import Customer

DATA_FILE = "data/customers.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_data(customers):
    with open(DATA_FILE, "w") as file:
        json.dump(customers, file, indent=4)

def add_customer(data):
    customers = load_data()
    customer = Customer(**data).to_dict()
    customers.append(customer)
    save_data(customers)
    return {"message": "Customer added successfully", "customer": customer}

def get_all_customers():
    return load_data()

def get_customer_by_id(id):
    customers = load_data()
    for c in customers:
        if c["id"] == id:
            return c
    return {"error": "Customer not found"}

def update_customer(id, data):
    customers = load_data()
    for c in customers:
        if c["id"] == id:
            c.update(data)
            save_data(customers)
            return {"message": "Customer updated", "customer": c}
    return {"error": "Customer not found"}

def delete_customer(id):
    customers = load_data()
    customers = [c for c in customers if c["id"] != id]
    save_data(customers)
    return {"message": "Customer deleted"}
