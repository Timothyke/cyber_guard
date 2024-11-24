NETWORK GUARD - PROJECT DOCUMENTATION

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
JavaScript: For dynamic functionality).
SQLite: The default database used by Django (can be changed to other databases like PostgreSQL or MySQL).

Installation & Setup

Python
Django
Nmap
Git 
A text editor (e.g., Visual Studio Code, PyCharm)

Steps to Install

1.	Clone the repository:

git clone https://github.com/Timothyke/cyber_guard.git
cd network-guard

3.	Create a virtual environment:
python -m venv venv

4.	Activate the virtual environment:
Windows:

venv\Scripts\activate
macOS/Linux:
source venv/bin/activate

5.	Install dependencies
   
pip install -r requirements.txt

7.	Install Nmap:

On Windows, download and install from nmap.org.
On Linux/macOS, you can install it via a package manager:
Ubuntu:
sudo apt install nmap
macOS:
brew install nmap

8.	Set up the database:

Run the following commands to apply migrations and set up the database:
python manage.py makemigrations
python manage.py migrate

9.	Create a superuser (to access the admin panel):
python manage.py createsuperuser

11.	Run the application:
python manage.py runserver
Navigate to http://127.0.0.1:8000/ in your browser to access the application.

Usage
•	Network Scanning
•	Login: Before accessing the network scan page, the user must log in via the login page (/login/).
•	Scan Network: Once logged in, navigate to the main page (/). Input the desired IP address and click on Scan to begin the scan.
•	View Results: After the scan is completed, the application will display a list of open ports on the specified IP address.
•	Admin Interface
•	Access the admin interface by navigating to /admin/.
•	Login with the superuser credentials created during setup.
•	The admin panel allows managing users and performing other administrative tasks.

