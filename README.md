# Cyber_Guard 🔒

**Cyber_Guard** is a dynamic web application built with Django, integrated with Nmap to perform network port scans, and implements Django's CRUD functionality to manage scan logs effectively. This project aims to provide a robust network security tool for monitoring open ports while allowing easy management of scan records.

---

## Features 🚀

- **Network Scanning**: Utilizes Nmap to scan IP addresses and detect open ports within a specified range.
- **CRUD Functionality**: Create, Read, Update, and Delete scan logs stored in a database.
- **User Authentication**: Secures the application with login/logout functionality.
- **Interactive Interface**: Displays scanning results and log management in a user-friendly format.
- **Deployable**: Configured to run on local environments and deployable to platforms like Heroku.

---

## Prerequisites and Dependencies 📋

Ensure you have the following installed before running the project:

### **System Requirements**
- Python (3.8 or higher recommended)
- Nmap installed on your system
  - **Installation**:
    - **Windows**: Download from [Nmap Official Site](https://nmap.org/download.html)
    - **Linux**: Install via your package manager:
      ```bash
      sudo apt install nmap
      ```
    - **Mac**: Install with Homebrew:
      ```bash
      brew install nmap
      ```

### **Python Libraries**
Install the following dependencies:
- `Django`
- `nmap` (Python wrapper for Nmap)
- Optional: `gunicorn` (for deployment)

---

## Installation and Setup 🔧

Follow these steps to get started:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Timothyke/cyber_guard.git
   cd cyber_guard
