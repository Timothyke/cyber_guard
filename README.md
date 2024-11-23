Network Guard - Project Documentation
Project Overview
Network Guard is a Django-based web application designed for network monitoring. The application allows users to scan and monitor IP addresses within a specified range, providing details on active devices and open ports. It also includes user authentication (login and logout) to ensure secure access.

Features
Network Scanning: Users can input an IP address, and the application will scan for open ports in the specified range (1-1024).
User Authentication: Includes login and logout functionality using Django's built-in authentication system.
Admin Interface: An admin interface provided by Django for managing users and other administrative tasks.
Technologies Used
Django: The primary framework used to build the web application.
nmap: A popular tool used to scan IPs for open ports.
HTML/CSS: For creating the user interface.
JavaScript: (Optional, if you plan to add dynamic functionality).
SQLite: The default database used by Django (can be changed to other databases like PostgreSQL or MySQL).
Installation & Setup
Prerequisites
Python (preferably Python 3.7+)
Django
Nmap
Git (optional, for version control)
A text editor (e.g., Visual Studio Code, PyCharm)
Steps to Install
Clone the repository (if you haven’t already):

bash
Copy code
git clone https://github.com/yourusername/network-guard.git
cd network-guard
Create a virtual environment (optional but recommended):

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

On Windows, download and install from nmap.org.
On Linux/macOS, you can install it via a package manager:
Ubuntu:
bash
Copy code
sudo apt install nmap
macOS:
bash
Copy code
brew install nmap
Set up the database:

Run the following commands to apply migrations and set up the database:
bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a superuser (to access the admin panel):

bash
Copy code
python manage.py createsuperuser
Run the application:

bash
Copy code
python manage.py runserver
Navigate to http://127.0.0.1:8000/ in your browser to access the application.

Usage
Network Scanning
Login: Before accessing the network scan page, the user must log in via the login page (/login/).
Scan Network: Once logged in, navigate to the main page (/). Input the desired IP address and click on Scan to begin the scan.
View Results: After the scan is completed, the application will display a list of open ports on the specified IP address.
Admin Interface
Access the admin interface by navigating to /admin/.
Login with the superuser credentials created during setup.
The admin panel allows managing users and performing other administrative tasks.
Project Structure
graphql
Copy code
network_guard/
├── network_monitor/        # Main app directory
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   │   ├── login.html      # Login page template
│   │   ├── scan_network.html # Network scan results page
│   ├── static/             # Static files like CSS and JS
│   ├── views.py            # Views that handle business logic
│   ├── urls.py             # URL routing for the network monitor app
├── cyber_guard/            # Main project folder
│   ├── settings.py         # Django settings
│   ├── urls.py             # Root URL routing
│   ├── wsgi.py             # WSGI configuration for deployment
├── manage.py               # Django management commands
├── requirements.txt        # List of project dependencies
├── db.sqlite3              # Default database file
Testing
Unit Tests
To run tests, use the following command:

bash
Copy code
python manage.py test
Unit tests are crucial for verifying the integrity of the core functionalities like network scanning and user authentication.

Integration Tests
Integration tests can be added to test the flow between multiple components (e.g., logging in and then scanning a network).
Future Enhancements
Support for more advanced nmap scanning options: Allow users to customize the port range or scanning options.
Port Details: Show more information about the open ports (e.g., service names, versions).
Support for different user roles: Add roles like Admin, User, and Viewer to control access to certain functionalities.
Error Handling: Implement better error handling for cases where an invalid IP is entered or the nmap scan fails.
Licenses & Credits
nmap: Used for network scanning, licensed under the Nmap License.
Django: Django is licensed under the BSD License.
Troubleshooting
nmap not found: Ensure that nmap is installed and correctly added to your system's PATH. You can verify by running nmap --version in the terminal.
Django error "No module named 'nmap'": If you encounter this error, ensure that you have the nmap Python package installed (pip install python-nmap).
