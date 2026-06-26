# 🔐 Password Security Analyzer

A production-ready password security analysis web application built with **Python**, **Flask**, and modern web technologies. The application evaluates password strength, estimates crack time, checks whether passwords have appeared in known data breaches using the **Have I Been Pwned API**, and delivers actionable security recommendations through a responsive, mobile-first interface.

## 🌐 Live Demo

**Live Application:** https://password-analyzer-yoap.onrender.com/

**GitHub Repository:** https://github.com/WhiteHatAnalystMike/Password-Security-Analyzer

---

## 📌 Overview

Weak passwords remain one of the most common causes of compromised accounts. This application helps users better understand password security by combining rule-based analysis, breach detection, and user-friendly feedback into a single web application.

The project demonstrates practical cybersecurity concepts alongside full-stack software development, deployment, and UI design.

---

## ✨ Features

* 🔒 Password strength analysis
* ⏱️ Password crack-time estimation
* 🚨 Compromised password detection using the Have I Been Pwned API
* 🧠 Actionable password improvement recommendations
* 🌙 Persistent Dark Mode
* 📱 Mobile-first iOS-inspired interface
* ⚡ Responsive Flask backend
* 🎨 Modern user experience with dynamic visual feedback

---

## 🛡 Cybersecurity Concepts Demonstrated

* Password strength evaluation
* Password complexity analysis
* Brute-force attack modeling
* Password crack-time estimation
* SHA-1 hashing
* k-Anonymity privacy model
* Secure API consumption
* Breached password detection
* Secure handling of sensitive user input (passwords are never stored)

---

## 🏗 System Architecture

```
                User
                  │
                  ▼
        Flask Web Application
                  │
      ┌───────────┴───────────┐
      │                       │
      ▼                       ▼
Password Analyzer      Breach Detection
(analyzer.py)         (HIBP API)
      │                       │
      └───────────┬───────────┘
                  ▼
          Jinja2 Templates
                  │
                  ▼
           Responsive UI
```

---

## 🛠 Tech Stack

| Category        | Technologies            |
| --------------- | ----------------------- |
| Language        | Python                  |
| Framework       | Flask                   |
| Frontend        | HTML5, CSS3, JavaScript |
| Templates       | Jinja2                  |
| Deployment      | Render                  |
| Version Control | Git & GitHub            |
| API             | Have I Been Pwned API   |

---

## 📂 Project Structure

```
Password-Security-Analyzer/
│
├── passwordanalyzer/
│   ├── analyzer.py
│   ├── breach_checker.py
│   ├── main.py
│   ├── templates/
│   │      └── index.html
│   └── static/
│          └── style.css
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Local Installation

### Clone the repository

```bash
git clone https://github.com/WhiteHatAnalystMike/Password-Security-Analyzer.git
cd Password-Security-Analyzer
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment

Windows

```bash
.venv\Scripts\activate
```

macOS / Linux

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python passwordanalyzer/main.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

> Add screenshots of:
>
> * Light Mode
> * Dark Mode
> * Password Analysis
> * Breach Detection Results

---

## 🎥 Demo

Watch the project demonstration:

https://youtu.be/7wIq1yjOJSA

---

## 🚀 Deployment

The application is deployed using **Render**.

Deployment highlights:

* Flask configured for production hosting
* Dynamic environment-based port configuration
* Dependency management with `requirements.txt`
* Automatic deployment from GitHub

---

## 📈 Future Improvements

* Password entropy calculation
* Secure password generator
* NIST password policy validation
* Animated password strength meter
* Password history (client-side only)
* Accessibility improvements
* Additional cybersecurity analysis tools

---

## 👨‍💻 Author

**Michael Koranteng**

Computer Science Student

Aspiring Cybersecurity Analyst

---

## ⭐ What This Project Demonstrates

* Python application development
* Flask web development
* REST API integration
* Secure software design principles
* Cybersecurity fundamentals
* Responsive UI/UX design
* Cloud deployment
* Git & GitHub workflows

---

## 📄 License

This project is available for educational and portfolio purposes.
