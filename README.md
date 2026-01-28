
# Customer Management System 

A **Customer Management System** built using **Python Flask** with a **web-based frontend**.
The project demonstrates **full CRUD (Create, Read, Update, Delete)** operations through RESTful APIs and a simple, user-friendly frontend interface.


##  Case Study Overview

This case study shows how a **modular Flask backend** can be integrated with a **frontend interface** to manage customer data efficiently.
The system is suitable for **API development practice, frontend–backend integration demos, and GitHub projects**.


##  Objectives

* Develop RESTful APIs using Flask
* Implement full CRUD operations
* Integrate frontend with backend APIs
* Use a modular project architecture
* Test APIs using Postman
* Create a professional GitHub-ready project


## Technologies Used

### Backend

* Python 3
* Flask Framework
* REST API
* JSON

### Frontend

* HTML5
* CSS3
* JavaScript (Fetch API)
* Jinja2 Templates

### Testing

* Postman


## Project Structure

```
customer_management_system/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── routes/
│   └── customer_routes.py
│
├── services/
│   └── customer_service.py
│
├── models/
│   └── customer_model.py
│
├── data/
│   └── customers.json
│
├── frontend/
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── style.css
│       └── script.js
│
└── tests/
    └── postman_collection.json
```


## Application Access

After starting the Flask server, open the application in a browser:

```
http://127.0.0.1:5000/
```


##  CRUD Operations

###  Create Customer

* Adds a new customer using the frontend form.
* Sends a **POST** request to the backend.

**Endpoint:** `/customers`


### Read Customers

* Fetches and displays all customers dynamically.

**Endpoint:** `/customers`

###  Update Customer

* Allows editing customer details via the UI.
* Sends a **PUT** request with updated data.

**Endpoint:** `/customers/{id}`


###  Delete Customer

* Deletes a customer using the delete button.
* Sends a **DELETE** request.

**Endpoint:** `/customers/{id}`

## CRUD Operations Summary

| Operation       | HTTP Method | Endpoint          | Description          |
| --------------- | ----------- | ----------------- | -------------------- |
| Create Customer | POST        | `/customers`      | Add new customer     |
| Read Customers  | GET         | `/customers`      | View all customers   |
| Update Customer | PUT         | `/customers/{id}` | Modify customer data |
| Delete Customer | DELETE      | `/customers/{id}` | Remove customer      |


##  API Testing with Postman

* A Postman collection is provided in the `tests/` folder.
* Import `postman_collection.json` into Postman.
* Execute CRUD operations independently from the frontend.


##  Key Features Demonstrated

* Full CRUD functionality
* RESTful API design
* Frontend–backend integration
* Jinja2 template rendering
* JSON-based data handling
* Modular Flask project structure
* API testing using Postman



