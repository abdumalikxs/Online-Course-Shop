# 🛍️ CourseShop

**Tech Stack:** Python, Django, SQLite3, HTML/CSS/JS, Tastypie API  
**Live Demo:** [bit.ly/abdu-shop](https://bit.ly/abdu-shop)  

---

## 📖 Overview

**CourseShop** is a scalable **online course platform** that supports category-based course listings, relational data models, and RESTful API endpoints.  
It was engineered for **speed, modular scalability, and clean API integration**, enabling users to browse, filter, and manage digital courses efficiently.

The project demonstrates robust **backend engineering**, **API design**, and **database modeling** using Django and Tastypie.

---

## 🚀 Key Highlights

- ⚙️ **Optimized Backend Performance**  
  Engineered backend workflows with efficient query handling and caching — achieving **page response times under 200 ms**.

- 🧩 **RESTful API Design & Testing**  
  Designed and tested **Tastypie REST APIs** using **Postman** for reliable CRUD operations on course and category resources.

- 🗂️ **Relational Models with Smart Cascade Logic**  
  Implemented models with **foreign-key relationships**, **cascade deletion**, **timestamps**, and **JSON serialization** for clean API output.

- 🔗 **Seamless URL Routing & Template Rendering**  
  Integrated Django’s routing and templating systems to ensure responsive UI rendering and modular scalability.

---

## 🖼️ Interface Preview

Below is a preview of the **Course List Page**, showing course titles, categories, prices, and enrollment data.

![Courses Shop UI](images/ui-screenshot.png)  
_(Insert your UI image — e.g., Screenshot 2025-10-27 at 18.51.41.png)_

### 🧪 API Testing (Postman)

You can view RESTful endpoints tested via Postman for course CRUD operations and serialization.

![Postman API Example](images/api-screenshot.png)  
_(Insert your Postman test screenshots here)_

---

## 🧠 Features

- Category-based course filtering and listings
- CRUD operations for Courses and Categories
- RESTful API endpoints with JSON responses
- Django Admin interface for managing content
- Relational database (SQLite3)
- Responsive HTML/CSS/JS front-end
- Clean separation of templates, views, and URLs

---

## 🧩 API Endpoints (Tastypie)

| Endpoint               | Method | Description               |
| ---------------------- | ------ | ------------------------- |
| `/api/v1/course/`      | GET    | Retrieve all courses      |
| `/api/v1/course/<id>/` | GET    | Retrieve a single course  |
| `/api/v1/course/`      | POST   | Create a new course       |
| `/api/v1/course/<id>/` | PUT    | Update an existing course |
| `/api/v1/course/<id>/` | DELETE | Delete a course           |

_All endpoints return JSON output serialized through Django Tastypie._

---

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/abdumalikxs/courseshop.git
cd courseshop
pipenv install
pipenv shell
python manage.py migrate
python manage.py runserver

Visit http://127.0.0.1:8000/ to view the app.

```
