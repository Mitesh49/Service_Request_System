# Service_Request_System
A web app where users can login and submit their request for services by mentioning the type and description of the service they want
Service Management System

This is a simple web application built using Streamlit for managing services. Users can log in, sign up, add new services, and view existing services.

Features:
- User authentication: Users can log in with their username and password. New users can sign up to create an account.
- Service management: Users can add new services with details such as service name, priority, type, and description.
- View existing services: All services, both newly added and previously existing, are displayed in the system.

Instructions:
1. Clone the repository or download the code files.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Streamlit application by executing `streamlit run app.py`.
4. Access the application in your web browser at the provided URL (usually http://localhost:8501).

File Structure:
- app.py: Contains the main Streamlit application code.
- login.xlsx: Excel file to store user credentials (username and hashed password).
- services.csv: CSV file to store service data (service name, priority, type, and description).
- requirements.txt: List of Python dependencies required for the project.

Dependencies:
- Streamlit: Web application framework for building interactive web applications.
- Pandas: Data manipulation library for handling tabular data.
- Hashlib: Library for hashing passwords.

Note: Ensure that you have Python installed on your system before running the application.
