# 🔐 Secure Coding Review – Task 3

## 📌 Project Overview

This project focuses on performing a secure coding review of a basic login system developed in Python. The goal is to identify security vulnerabilities in an insecure implementation and improve it using secure coding practices.

---

## 🎯 Objectives

* Perform a security audit of the application
* Identify common coding vulnerabilities
* Apply secure coding techniques
* Provide recommendations and remediation steps

---

## 🗂️ Project Structure

* insecure.py – Vulnerable implementation
* secure.py – Improved secure version
* README.md – Project documentation

---

## 🚨 Vulnerabilities Identified

* Use of plain text credentials
* No password encryption or hashing
* Hardcoded sensitive data
* Unlimited login attempts (brute force risk)
* Lack of input validation

---

## 🔒 Security Improvements

* Implementation of password hashing
* Restriction on login attempts
* Improved authentication logic
* Reduced exposure of sensitive data

---

## 🛡️ Recommended Best Practices

* Use strong hashing algorithms like bcrypt or Argon2
* Add salting to passwords
* Store credentials securely in a database
* Avoid hardcoding sensitive information
* Implement input validation and sanitization
* Enable logging and monitoring
* Use multi-factor authentication (MFA)

---

## 🧰 Tools & Techniques

* Python
* Manual Code Review
* Basic Security Analysis

---

## 📊 Conclusion

The insecure version contained several critical vulnerabilities that could lead to unauthorized access. The secure version improves the system by applying hashing and limiting login attempts, making it significantly more secure.

---

## 👨‍💻 Author

Yash Tambe
