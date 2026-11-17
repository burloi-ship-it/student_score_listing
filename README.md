# 🎓 Student Records Management System (CLI)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Pickle](https://img.shields.io/badge/Serialization-Pickle-orange?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interface-CLI-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

*A robust Command Line Interface (CLI) application for student record management, built in Python with data persistence and advanced input validations.*

</div>

---

## 📋 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Installation and Execution](#-installation-and-execution)
- [Example Usage](#-example-usage)
- [Concepts Demonstrated](#-concepts-demonstrated)

---

## 🚀 About the Project

This project is a complete and simple student record management system. Designed as a Command Line Interface (CLI) application, it allows users to add, view, filter, and delete records efficiently.

The application uses **object serialization** (via the `pickle` module) to ensure data persistence between sessions, automatically saving information to a local binary file.

---

## ✨ Key Features

- **📂 Data Persistence:** Automatic saving and loading of records using binary files (`pickle`).
- **👥 General View:** Lists all registered students in the system with automatic numbering.
- **➕ Secure Addition:** 
  - Validates that student names contain only letters and spaces (no numbers or special characters).
  - Prevents empty input fields.
- **❌ Controlled Deletion:** Allows removing a specific student based on their list sequence number.
- **🔍 Advanced Filtering:** Quick view of students who achieved a score greater than or equal to 7.
- **📋 Name List:** Extracts and displays only the names of available students in the system.
- **🧹 Data Reset:** Secure option (with `Y/N` confirmation) to completely clear the local database.

---

## 🛠️ Technologies Used

* **Language:** `Python 3.x`
* **Standard Modules:** 
  * `os` — for checking and managing local files.
  * `pickle` — for object serialization and deserialization.
* **Architecture:** Object-Oriented Programming (OOP) using the custom `Log` class.

---

## 📂 Project Structure

```text
📁 student-management-system/
│
├── 📄 main.py          # Main script containing the interactive CLI loop
├── 📄 log.py           # Definition of the Log class (student data model)
└── 📄 README.md        # Project documentation

⭐ If you found this project useful, consider giving it a star!
