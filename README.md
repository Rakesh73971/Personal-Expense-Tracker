
# 💰 Expense Tracker API

A **Django REST Framework (DRF)**–based backend API for managing daily expenses.
This project helps users categorize their expenses, track total spending, and easily filter transactions by category or payment method.

---

## 🚀 Features

### 🧩 Core Features

* **Category Management**

  * Create, update, delete, and view expense categories (e.g., Food, Travel, Bills).

* **Expense Management**

  * Add, update, delete, and list expenses.
  * Assign expenses to specific categories.

* **Filter & Total Calculation**

  * Filter expenses by category, date, or payment method.
  * Automatically calculate the total amount of expenses.
  * Supports filtered total endpoints (e.g., total by category or payment method).

* **RESTful Endpoints**

  * Clean and structured API design following REST principles.

---

## ⚙️ Technologies Used

* **Backend:** Python, Django, Django REST Framework
* **Database:** SQLite (default, easy to configure)
* **Filtering:** `django-filter`
* **Tools:** Git, GitHub, VS Code

---

## 🧭 API Design Overview

| Resource               | Endpoint                                    | Description                               |
| ---------------------- | ------------------------------------------- | ----------------------------------------- |
| **Category**           | `/categories/`                              | List all categories or create a new one   |
| **Category Detail**    | `/categories/{id}/`                         | Retrieve, update, or delete a category    |
| **Expense**            | `/expenses/`                                | List all expenses or create a new expense |
| **Expense Detail**     | `/expenses/{id}/`                           | Retrieve, update, or delete an expense    |
| **Expense with Total** | `/expenses/with-total/`                     | View filtered expenses with total amount  |
| **Filter by Category** | `/expenses/with-total/?category=1`          | Get total sum of expenses for category 1  |
| **Filter by Payment**  | `/expenses/with-total/?payment_method=Cash` | Get total sum of expenses paid by Cash    |



## 💻 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/expense-tracker-api.git
cd expense-tracker-api
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv env
```

### 3️⃣ Activate the Environment

* **Windows:**

```bash
env\Scripts\activate
```

* **Mac/Linux:**

```bash
source env/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run Migrations

```bash
python manage.py migrate
```

### 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

Server will start at → **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🧾 Sample Input & Output

### ➕ Add Category (POST `/categories/`)

**Request:**

```json
{
  "name": "Food"
}
```

**Response:**

```json
{
  "id": 1,
  "name": "Food"
}
```

---

### ➕ Add Expense (POST `/expenses/`)

**Request:**

```json
{
  "category": 1,
  "title": "Lunch at cafe",
  "amount": 250.00,
  "date": "2025-10-05",
  "payment_method": "Cash",
  "note": "Weekend lunch"
}
```

**Response:**

```json
{
  "id": 1,
  "category": 1,
  "title": "Lunch at cafe",
  "amount": 250.0,
  "date": "2025-10-05",
  "payment_method": "Cash",
  "note": "Weekend lunch"
}
```

---

### 📊 Get Expenses with Total (GET `/expenses/with-total/`)

**Response:**

```json
{
  "Expenses": [
    {
      "id": 1,
      "category": "Food",
      "title": "Lunch at cafe",
      "amount": 250.0,
      "date": "2025-10-05",
      "payment_method": "Cash",
      "note": "Weekend lunch"
    },
    {
      "id": 2,
      "category": "Travel",
      "title": "Bus Ticket",
      "amount": 50.0,
      "date": "2025-10-05",
      "payment_method": "Card",
      "note": "Local trip"
    }
  ],
  "total_amount": 300.0
}
```

---

### 📊 Get Total by Category (GET `/expenses/with-total/?category=1`)

**Response:**

```json
{
  "Expenses": [
    {
      "id": 1,
      "category": "Food",
      "title": "Lunch at cafe",
      "amount": 250.0,
      "date": "2025-10-05",
      "payment_method": "Cash",
      "note": "Weekend lunch"
    }
  ],
  "total_amount": 250.0
}
```

---

### 📊 Get Total by Payment Method (GET `/expenses/with-total/?payment_method=Cash`)

**Response:**

```json
{
  "Expenses": [
    {
      "id": 1,
      "category": "Food",
      "title": "Lunch at cafe",
      "amount": 250.0,
      "date": "2025-10-05",
      "payment_method": "Cash",
      "note": "Weekend lunch"
    }
  ],
  "total_amount": 250.0
}
```

---

## 🧠 Short Design Documentation

* **Models:**

  * `Category`: Stores expense categories (e.g., Food, Rent, Travel)
  * `Expense`: Stores individual expenses linked to a category

* **Serializers:**

  * Handle validation, including checks for empty names or invalid values
  * `ExpenseSerializer` supports showing **category name** while accepting **category ID** for POST

* **Views:**

  * `CategoryViewSet`: Full CRUD API for categories
  * `ExpenseViewSet`: CRUD + filter + total calculation endpoints

* **Routers:**

  * Uses `DefaultRouter` for clean REST API endpoints

* **Filtering:**

  * Implemented using `django-filter`
  * Supports filtering expenses by category, date, or payment method

---




