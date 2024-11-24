
🌐 Network Guard 🚀
A Powerful Django-Based Web Application for Network Monitoring & Security

📖 Project Overview
Network Guard is a robust and user-friendly web application designed to make network monitoring a breeze. Built with Django, it enables users to:
✅ Scan and monitor IP addresses within a specified range.
✅ Identify active devices and open ports.
✅ Access features securely with user authentication.

✨ Key Features
🌟 Network Scanning:

Input an IP address to scan for open ports in the range (1–1024).
🔒 User Authentication:

Secure login and logout functionality using Django’s built-in authentication system.
⚙️ Admin Interface:

Manage users and administrative tasks through Django's powerful admin panel.
🛠️ Technologies Used
Django: 🌟 Web framework powering the application.
Nmap: 🔍 Network scanning tool for identifying open ports.
HTML/CSS: 🎨 Creating a sleek and responsive user interface.
JavaScript: ⚡ Adding dynamic functionality.
SQLite: 🗄️ Default database (switchable to PostgreSQL/MySQL).
⚙️ Installation & Setup
Prerequisites
🖥️ Python | 🔗 Django | 🔍 Nmap | 📁 Git | ✏️ Text Editor (e.g., VS Code, PyCharm)

Steps to Install
Clone the repository:

bash
Copy code
git clone https://github.com/Timothyke/cyber_guard.git  
cd network-guard  
Create a virtual environment:

bash
Copy code
python -m venv venv  
Activate the virtual environment:

Windows:
bash
Copy code
venv\Scripts\activate  
macOS/Linux:
bash
Copy code
source venv/bin/activate  
Install dependencies:

bash
Copy code
pip install -r requirements.txt  
Install Nmap:

Windows: Download and install from nmap.org.
Linux/macOS: Install via a package manager:
Ubuntu:
bash
Copy code
sudo apt install nmap  
macOS:
bash
Copy code
brew install nmap  
Set up the database:

bash
Copy code
python manage.py makemigrations  
python manage.py migrate  
Create a superuser (for admin access):

bash
Copy code
python manage.py createsuperuser  
Run the application:

bash
Copy code
python manage.py runserver  
🌐 Navigate to http://127.0.0.1:8000/ to access the application.

🚀 Usage
Network Scanning
🔑 Login: Access the login page via /login/ to authenticate.
🌐 Scan Network: Input an IP address and click "Scan" to identify open ports.
📊 View Results: See the list of open ports on the specified IP address.

Admin Interface
⚙️ Admin Dashboard: Visit /admin/ for user management and administrative tasks.
🔑 Login with the superuser credentials created earlier.

📂 File Structure
Here's a quick overview of the file structure:

php
Copy code
📁 network-guard/  
├── 📁 app/        # Django app files  
├── 📁 templates/  # HTML templates  
├── 📁 static/     # CSS & JS files  
├── manage.py      # Django management script  
└── requirements.txt # Project dependencies  
🤝 Contributions
🎉 Contributions are welcome! Feel free to fork this repository and create pull requests.
💬 Have questions or suggestions? Open an issue, and we’ll get back to you ASAP!

💻 Stay Connected
📧 Email: timothymaina040@gmail.com
🌐 GitHub: Timothyke

🌟 Show Your Support
⭐️ If you like this project, give it a star on GitHub!
🚀 Let’s build the future of secure network monitoring together!

