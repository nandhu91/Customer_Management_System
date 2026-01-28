from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)

DATA_FILE = "data/customers.json"

def load_customers():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_customers(customers):
    with open(DATA_FILE, "w") as file:
        json.dump(customers, file, indent=4)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/customers', methods=['POST'])
def add_customer():
    customers = load_customers()
    data = request.json
    customers.append(data)
    save_customers(customers)
    return jsonify({"message": "Customer added", "customer": data})

@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(load_customers())

@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    customers = load_customers()
    data = request.json
    for c in customers:
        if c["id"] == id:
            c.update(data)
            save_customers(customers)
            return jsonify({"message": "Customer updated", "customer": c})
    return jsonify({"error": "Customer not found"}), 404

@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customers = load_customers()
    customers = [c for c in customers if c["id"] != id]
    save_customers(customers)
    return jsonify({"message": "Customer deleted"})

if __name__ == "__main__":
    app.run(debug=True)
