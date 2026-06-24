# 🔐 Password Security Analyzer

> A production-ready web application that analyzes password strength, estimates crack time, and provides actionable security feedback — built with a mobile-first, iOS-inspired interface.

🌐 **Live Demo:** https://password-analyzer-yoap.onrender.com/
📦 **Repository:** https://github.com/WhiteHatAnalystMike/Password-Security-Analyzer

---

## ✨ Overview

The Password Security Analyzer is a full-stack web application designed to simulate real-world password security evaluation. It helps users understand how secure their passwords are by combining scoring logic, crack-time estimation, and user-friendly feedback.

This project emphasizes both **cybersecurity fundamentals** and **modern UI/UX design**, delivering a tool that is both functional and intuitive.

---

## 🎯 Key Features

* 🔍 **Real-Time Password Strength Analysis**
* ⏱️ **Estimated Crack Time Calculation**
* 🧠 **Context-Aware Security Feedback**
* 🌙 **Dark Mode (Persistent via Local Storage)**
* 📱 **Mobile-First iOS-Style UI**
* ⚡ **Lightweight & Fast Flask Backend**
* 🔄 **Interactive UX with Dynamic Updates**

---

## 🧠 Engineering Highlights

* Designed and implemented a **rule-based password strength scoring algorithm** evaluating length, character diversity, and complexity
* Modeled **estimated brute-force crack times** based on password strength
* Built a **responsive, mobile-first UI** mimicking native iOS design patterns
* Implemented **client-side state persistence** using `localStorage` for theme preference
* Structured application using **modular Flask architecture**

---

## 🏗️ System Architecture

```text
User Input (Browser)
        ↓
Flask Backend (main.py)
        ↓
Password Analysis Engine (analyzer.py)
        ↓
Rendered UI (Jinja Templates)
```

---

## 🛠️ Tech Stack

| Layer      | Technology               |
| ---------- | ------------------------ |
| Backend    | Python, Flask            |
| Frontend   | HTML, CSS (iOS-style UI) |
| Deployment | Render                   |
| Versioning | Git & GitHub             |

---

## 📂 Project Structure

```text
Password-Security-Analyzer/
│
├── passwordanalyzer/
│   ├── main.py          # Flask app entry point
│   ├── analyzer.py      # Password scoring logic
│   ├── templates/
│   │   └── index.html   # UI layout
│   ├── static/
│   │   └── style.css    # iOS-style UI styling
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Local Development

### 1. Clone repository

```bash
git clone https://github.com/WhiteHatAnalystMike/Password-Security-Analyzer.git
cd Password-Security-Analyzer
```

### 2. Setup environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run application

```bash
python passwordanalyzer/main.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## 🔒 Security Concepts Demonstrated

* Password strength heuristics
* Brute-force attack modeling
* Crack-time estimation logic
* Secure input handling (no persistence of sensitive data)
* User-centered security design

---

## 📸 Screenshots

*(Add screenshots here for maximum impact)*

```text
screenshots/light.png
screenshots/dark.png
```

---

## 📸 Demo

🎥 Watch the demo here:
https://youtu.be/7wIq1yjOJSA

---

## 🚀 Deployment

This application is deployed on Render using a Python web service.

Key deployment considerations:

* Bound Flask to `0.0.0.0` for external access
* Used environment-based port configuration
* Managed dependencies via `requirements.txt`

---

## 📈 Future Enhancements

* Integrate **HaveIBeenPwned API** for breach detection
* Implement **entropy-based scoring algorithm**
* Add **user authentication & saved history**
* Introduce **real-time animations & transitions**
* Expand into a **full cybersecurity toolkit**

---

## 👤 Author

**Michael Koranteng**
Computer Science Student | Aspiring Cybersecurity Analyst

---

## 💼 Resume Highlights

* Built and deployed a **full-stack password security analyzer** using Flask and custom scoring algorithms
* Implemented **real-time password evaluation** with crack-time estimation and actionable feedback
* Designed a **mobile-first, iOS-inspired UI** with dark mode and persistent user preferences
* Deployed a **production-ready web application** on Render with proper environment configuration

---

## ⭐️ Impact

This project demonstrates:

* Full-stack development capability
* Deployment & DevOps understanding
* UI/UX design awareness
* Cybersecurity fundamentals

---

## 📌 Why This Project Matters

Weak passwords remain one of the most common security vulnerabilities.
This tool bridges the gap between **technical security concepts** and **user-friendly design**, helping users make better security decisions in real time.

---

⭐️ If you found this useful, consider starring the repository.

