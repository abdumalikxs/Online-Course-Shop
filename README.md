# 🛍️ CourseShop

**Tech Stack:** Python, Django, SQLite3, HTML/CSS/JS, Tastypie API  
**Live Demo:**  https://courseshop.pythonanywhere.com

---

## 📖 Overview

**CourseShop** is a scalable **online course platform** that supports category-based course listings, relational data models, and RESTful API endpoints.  
It was engineered for **speed, modular scalability, and clean API integration**, enabling users to browse, filter, and manage digital courses efficiently.

The project demonstrates robust **backend engineering**, **API design**, and **database modeling** using Django and Tastypie.

---

## 🚀 Key Highlights

- ⚙️ **Optimized Backend Performance**  
  Engineered backend workflows with efficient query handling and caching, achieving supe-fast page response time.

- 🧩 **RESTful API Design & Testing**  
  Designed and tested **Tastypie REST APIs** using **Postman** for reliable CRUD operations on course and category resources.

- 🗂️ **Relational Models with Smart Cascade Logic**  
  Implemented models with **foreign-key relationships**, **cascade deletion**, **timestamps**, and **JSON serialization** for clean API output.

- 🔗 **Seamless URL Routing & Template Rendering**  
  Integrated Django’s routing and templating systems to ensure responsive UI rendering and modular scalability.

- 🔒 **Secure API Access Control**  
  Implemented API-key authentication in Tastypie, restricting write operations (POST, PUT, PATCH, DELETE) to authorized users while keeping GET requests public for safe data browsing.
  

---

## 🖼️ Interface Preview

Below is a preview of the **Course List Page**, showing course titles, categories, prices, and enrollment data.

<img width="1440" height="815" alt="Screenshot 2025-10-27 at 19 08 55" src="https://github.com/user-attachments/assets/87562467-d7ac-4233-a71b-cda47e76169c" />

### 🧪 API Testing (Postman)

You can view RESTful endpoints tested via Postman for course CRUD operations and serialization.

<img width="1440" height="900" alt="Screenshot 2025-10-27 at 19 39 02" src="https://github.com/user-attachments/assets/2bc47a20-6335-43f4-b514-2c159fb3524a" />
<img width="1440" height="900" alt="Screenshot 2025-10-27 at 19 37 00" src="https://github.com/user-attachments/assets/963b3461-6567-4caf-b5e6-ee70ddb4c7e4" />
<img width="1440" height="900" alt="Screenshot 2025-10-27 at 19 12 05" src="https://github.com/user-attachments/assets/e6ad6b46-ff46-4878-bd45-e59ee5c757e8" />
<img width="1440" height="900" alt="Screenshot 2025-10-27 at 19 33 39" src="https://github.com/user-attachments/assets/c21799db-3bb9-4974-8a21-0fa6697a1ac9" />
<img width="1440" height="900" alt="Screenshot 2025-10-27 at 19 36 39" src="https://github.com/user-attachments/assets/d9a94ce2-9847-4fb1-a4af-0db097116525" />



---

## 🧠 Features

- Category-based course filtering and listings
- CRUD operations for Courses and Categories
- RESTful API endpoints with JSON responses
- Django Admin interface for managing content
- Relational database (SQLite3)
- Responsive HTML/CSS/JS front-end
- Clean separation of templates, views, and URLs
- 🔐 **Authentication layer added:** All POST, PUT, and DELETE requests require API-key authentication; only GET requests are public.

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
