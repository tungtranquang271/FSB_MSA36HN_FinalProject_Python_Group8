# 🎓 FSB_MSA36HN – Python Final Project (Group 8)

## 📊 Student Management & Data Analysis System

## 🚀 Project Overview

A **Python-based system** for managing and analyzing student data, developed to fulfill the requirements of the **FSB_MSA36HN** course.

The project includes:

* 🔧 **Backend API** for student management
* 🖥️ **Desktop Application (FE3)** for data crawling, preprocessing, analysis, and visualization

## 📝 Functional Requirements

### 👨‍🎓 Student Information

* Student ID
* First name, Last name
* Email
* Date of birth
* Hometown
* Math, Literature, English scores

### ⚙️ System Features

* CRUD operations for students
* API returns student data in JSON format
* Support missing or incomplete data
* Preloaded dataset of **100 students**

---

## 🏗️ System Architecture

```
Backend (FastAPI + MongoDB)
        ↓
REST API (JSON)
        ↓
Desktop App (PyQt5)
        ↓
Crawl → Save Text File → Pandas Preprocessing → Analysis → Visualization
```

---

## 🧰 Technologies Used

### 🔙 Backend

* 🐍 Python 3.10+
* ⚡ FastAPI
* ☁️ MongoDB Atlas
* 🔌 PyMongo
* 🔐 python-dotenv

### 🖥️ Frontend (FE3 – Desktop App)

* 🧩 PyQt5
* 🌐 Requests
* 🧮 Pandas
* 📈 Matplotlib
* 🔢 NumPy

---

## 📂 Project Structure

### Backend

```
backend/
├── app/
│   ├── api/
│   ├── services/
│   ├── repositories/
│   ├── models/
│   ├── core/
│   └── main.py
├── .env
└── requirements.txt
```

### Desktop App (FE3)

```
desktop_app/
├── main.py
├── config.py
├── api/
├── crawler/
├── storage/
├── preprocessing/
├── analysis/
├── visualization/
├── ui/
├── data/
└── requirements.txt
```

---

## 🔄 FE3 Data Processing Workflow

1. 🔎 Crawl student data from Backend API
2. 💾 Save data to text file
3. 🧹 Clean and normalize data using Pandas
4. 📊 Perform data analysis
5. 📈 Visualize results using charts

---

## ▶️ How to Run

### 🔧 Backend

```bash
cd backend
uvicorn app.main:app --reload
```

📍 API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 🖥️ Desktop App (FE3)

```bash
cd desktop_app
python main.py
```

---

## 📊 Data Analysis & Visualization

* 📌 Average score comparison by hometown
* 📌 Score distribution analysis
* 📌 Math vs English comparison

**Charts used:**

* Bar Chart
* Grouped Bar Chart
* Box Plot (advanced analysis)

---

## ✅ Conclusion

* ✔ Fully meets the project requirements
* ✔ Clear separation between Backend and FE3
* ✔ Effective use of Pandas for data preprocessing and analysis
* ✔ Desktop application is intuitive and extensible

---
