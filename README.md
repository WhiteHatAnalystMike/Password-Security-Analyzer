# 🔐 Password Security Analyzer

A Flask-based cybersecurity web application that analyzes password strength, estimates password crack time, and checks whether a password has appeared in known data breaches using the **Have I Been Pwned (HIBP) API**.

Unlike a basic password checker, this application combines password strength analysis, crack-time estimation, and real-world breach detection into a single tool designed to help users make more informed security decisions.

I built this project to strengthen my Python, Flask, and cybersecurity skills while gaining **hands-on experience** designing, developing, and deploying a full-stack web application.

🌐 **Live Demo:** https://password-analyzer-yoap.onrender.com/

📦 **GitHub Repository:** https://github.com/WhiteHatAnalystMike/Password-Security-Analyzer

---

## Overview

Weak passwords continue to be one of the most common causes of compromised accounts. The goal of this project is to help users better understand the security of their passwords by providing real-time analysis, estimating how long a password would take to crack, and checking whether it has appeared in publicly known data breaches.

While building this application, I focused on writing clean, **maintainable** code, integrating external APIs, and creating a responsive interface that is intuitive and easy to use.

---

## 📸 Application Preview

### Home Screen (Light Mode)

The application opens with a clean, mobile-friendly interface where users can enter a password, switch between light and dark mode, and begin an analysis.

![Home Screen - Light](assets/screenshots/home-light.png)

---

### Home Screen (Dark Mode)

The application also supports a persistent dark mode, allowing users to switch themes while maintaining the same responsive experience.

![Home Screen - Dark](assets/screenshots/home-dark.png)

---

### Strong Password Analysis

A strong password receives the highest security score, an estimated crack time, and confirmation that it has not appeared in known public data breaches.

![Strong Password](assets/screenshots/strong-password-light.png)

---

### Breached Password Detection

If a password has appeared in previous data breaches, the application alerts the user, displays the number of known breaches, and provides recommendations to improve password security.

![Breached Password](assets/screenshots/breached-password-light.png)

---

## Features

* 🔐 Analyze password strength
* ⏱️ Estimate password crack time
* 🌐 Detect breached passwords using the **Have I Been Pwned (HIBP) API**
* 💡 Generate personalized security recommendations
* 🌙 Toggle between Light and Dark Mode
* 📱 Responsive interface for desktop and mobile devices
* ⚡ Fast Flask backend with dynamic updates

---

## Technologies Used

| Category        | Technology                   |
| --------------- | ---------------------------- |
| Language        | Python                       |
| Framework       | Flask                        |
| Frontend        | HTML, CSS, JavaScript        |
| API             | Have I Been Pwned (HIBP) API |
| Deployment      | Render                       |
| Version Control | Git & GitHub                 |

---

## What I Learned

Building this project gave me hands-on experience with:

* Developing a full-stack web application using Flask
* Organizing Python code into reusable modules
* Integrating a third-party REST API (Have I Been Pwned)
* Deploying a Python application with Render
* Using Git and GitHub for version control
* Applying cybersecurity concepts to a real-world application
* Designing responsive user interfaces with HTML, CSS, and JavaScript
* Debugging and solving real-world development challenges

---

## Project Structure

```text
Password-Security-Analyzer/
│
├── assets/
│   └── screenshots/
│       ├── home-light.png
│       ├── home-dark.png
│       ├── strong-password-light.png
│       ├── strong-password-dark.png
│       ├── breached-password-light.png
│       └── breached-password-dark.png
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── analyzer.py           # Password strength analysis
├── breach_checker.py     # HIBP API integration
├── main.py               # Flask application entry point
├── requirements.txt      # Python dependencies
├── .gitignore
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/WhiteHatAnalystMike/Password-Security-Analyzer.git
```

### 2. Navigate to the project directory

```bash
cd Password-Security-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python main.py
```

### 7. Open your browser

```text
http://127.0.0.1:5000
```

---

## Security Concepts Demonstrated

This project demonstrates several cybersecurity concepts, including:

* Password strength evaluation
* Password complexity analysis
* Password crack-time estimation
* Secure handling of user input
* Password breach detection using the Have I Been Pwned API
* The HIBP k-Anonymity model, which allows passwords to be checked without transmitting the complete password

---

## Deployment

The application is deployed on **Render** and is publicly accessible through the live demo link above.

Deployment includes:

* Flask production configuration
* Dependency management with `requirements.txt`
* Environment-based configuration
* Git and GitHub version control
* Cloud deployment using Render

---

## Future Improvements

Some features I plan to add include:

* 🔑 Secure password generator
* 📊 Password entropy calculations
* 📈 Password strength history
* 📁 Exportable security reports
* 🌍 Multi-language support
* 🛡️ Additional cybersecurity tools and utilities

---

## About Me

**Michael Koranteng**

Computer Science student at Towson University with a strong interest in cybersecurity, software engineering, and building secure, user-focused applications. I enjoy learning new technologies and applying them through hands-on projects.

**GitHub:** https://github.com/WhiteHatAnalystMike

---

## Why I Built This Project

This project was my **first application built with Python, JavaScript, and HTML**. My goal was to strengthen my software development skills while learning more about cybersecurity, API integration, and full-stack web development.

Building this application challenged me to learn new technologies, solve real-world problems, and create a project that demonstrates both my technical skills and my interest in cybersecurity.

If you have any suggestions or feedback, feel free to open an issue or reach out.

