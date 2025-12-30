# 🎓 FSB_MSA36HN – Python Final Project (Group 8)

## 📊 Student Management & Data Analysis System

## 🚀 Project Overview

A Python-based system developed for the **FSB_MSA36HN** course, focusing on student data management and data analysis.

The project consists of:

* 🔧 Backend API for managing student information
* 🖥️ Desktop Application (FE3) for data crawling, preprocessing, analysis, and visualization

## 📝 Functional Requirements

**Student information includes:**

* Student ID
* First name, Last name
* Email
* Date of birth
* Hometown
* Math, Literature, English scores

**System features:**

* CRUD operations for students
* REST API returning JSON data
* Support for missing or incomplete data
* Preloaded dataset of 100 students

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

## 🧰 Technologies Used

**Backend**

* 🐍 Python 3.10+
* ⚡ FastAPI
* ☁️ MongoDB Atlas
* 🔌 PyMongo
* 🔐 python-dotenv

**Frontend (FE3 – Desktop App)**

* 🧩 PyQt5
* 🌐 Requests
* 🧮 Pandas
* 📈 Matplotlib
* 🔢 NumPy

## 📂 Project Structure

**Backend**

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

**Desktop App (FE3)**

```
desktop_app/
├── analysis/          # Data analysis using Pandas (statistics, comparison, correlation)
├── api/               # API client layer (call backend APIs)
├── crawler/           # Crawl student data from backend APIs
├── preprocessing/     # Data cleaning & normalization (Pandas)
├── storage/           # Local file storage (students.txt)
├── ui/                # PyQt5 user interface (windows, buttons, layouts)
├── visualization/     # Data visualization (bar chart, scatter, performance chart)
├── .gitignore         # Ignore virtual env, cache, data files
├── main.py            # Application entry point
├── requirements.txt   # Python dependencies
└── students.txt       # Crawled student data (generated locally)
```

## 🔄 FE3 Data Processing Workflow

1. Crawl student data from Backend API
2. Save data to a text file
3. Clean and normalize data using Pandas
4. Perform data analysis
5. Visualize results using charts

## ▶️ How to Run

**Backend**

```bash
cd backend
uvicorn app.main:app --reload
```

API documentation available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

**Desktop App (FE3)**

```bash
cd desktop_app
python main.py
```

## ✅ Conclusion

* Fully meets project requirements
* Clear separation between Backend and FE3
* Effective use of Pandas for preprocessing and analysis
* Desktop application is intuitive and extensible
