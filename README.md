# ⚡ Household Energy Consumption Tracker 🔌

Hello! I'm **Sujata** 👩‍💻, and this is an interactive Python-MySQL based console application to **monitor**, **log**, and **analyze** household energy usage with real-time bill calculation and user summaries.

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0-lightgrey.svg)
![ConsoleApp](https://img.shields.io/badge/Interface-Console-green)
![ProjectStatus](https://img.shields.io/badge/Status-Completed-brightgreen)

---
## 🏁 📄 View main.py Script

[https://drive.google.com/file/d/1neifbDAad6Nd-ewEV_3gRu85D4zbcjnl/view?usp=drive_link]


---

## 🧠 Idea Behind the Project

The **Household Energy Consumption Tracker** is a backend-focused, console-based system that allows users to be added and tracked for their energy usage. It dynamically calculates electricity bills using tiered pricing and generates summarized reports per user, helping promote energy efficiency and strategic usage.

---

## 🚀 Key Features

- 👤 **Add New Users** (with name, address, email)
- 📊 **Log Daily Energy Consumption**
- 💰 **Auto-Calculate Bills** based on units consumed
- 📅 **View Historical Consumption Summary**
- 🧾 **Generate Consolidated Reports** per user
- 💻 **Console-based Interactive UI**
- 💾 **MySQL Backend Integration**

---

## 📈 Insights & Strategic Use

This tracker helps households:
- Monitor daily or monthly consumption.
- Detect high-usage patterns.
- Analyze cost implications of usage.
- Make informed energy-saving decisions.
- Prepare for smarter bill planning.

---

## 🧱 Database Schema


📁 Database: energy_tracker

📍 **Table: users**

user_id (PK)

name

address

email

📍 **Table: energy_usage**

log_id (Primary Key)

user_id (Foreign Key)

date

units_consumed

amount



---

## 📦 Core Technologies

| Component        | Technology        |
|------------------|-------------------|
| Language         | Python 3.10        |
| Database         | MySQL 8.0          |
| IDE              | VS Code            |
| Connector        | mysql-connector-python |
| UI               | Console (CLI)      |

---


## 🤓 What I Learned

- Integrated Python with MySQL for full-stack backend development.
- Applied real-world logic like tiered billing in code.
- Practiced exception handling, modular code.
- Understood relational schema design and foreign key relationships.
- Built a complete CRUD-based application using structured programming.

  ---

## 📁 Project Structure
  **Household_Energy_Consumption_Tracker/
├── 📄 energy_tracker_console.py   
├── 📁 database/
│   └── 📄 schema.sql                 
├── 📁 docs/
│   └── 📄 README.md              
│   └── 📄 insights.txt  
├── 📁 screenshots/                   
└── 📄 requirements.txt           

---
## 🙏 Gratitude
A special thanks to my mentor **Miss Sheetal Gupta** and my institute **SkillCircle** for their guidance and support throughout this project.

--- 
## 🤝 Get in Touch

I'd love to connect and collaborate on data-driven projects, analytics roles, or anything related to insights and innovation. Feel free to reach out!

📧 **Email** [sujataattri5@gmail.com]

💼 **LinkedIn** [www.linkedin.com/in/sujata-ab727236a]

🐙 **GitHub** [https://github.com/Sujata1204]

---
## ⭐ Feedback and Support

If you found this project helpful or have suggestions, feel free to open an issue or connect with me!

---
## ⚡ "Monitor every unit, manage every rupee — power up your savings with smart tracking!"
