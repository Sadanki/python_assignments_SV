# Python Assignments

This repository contains various Python assignments focused on DevOps, security, and infrastructure management.

## Projects

### 1. Password Strength Checker
- **Objective**: Ensure strong passwords to enhance security.
- **Tasks**:
  - Implement a Python function `check_password_strength` that takes a password string as input.
  - Check the password against the following criteria:
    - Minimum length: At least 8 characters.
    - Contains both uppercase and lowercase letters.
    - Contains at least one digit (0-9).
    - Contains at least one special character (e.g., !, @, #, $, %).
  - Return a boolean value indicating whether the password meets the criteria.
  - Write a script that takes user input for a password and calls the `check_password_strength` function to validate it.
  - Provide appropriate feedback to the user based on the strength of the password.

### 2. CPU Health Monitor
- **Objective**: Monitor the health and performance of servers by tracking CPU usage.
- **Tasks**:
  - Continuously monitor the CPU usage of the local machine.
  - Display an alert message if the CPU usage exceeds a predefined threshold (e.g., 80%).
  - Run indefinitely until interrupted.
  - Include appropriate error handling to manage exceptions that may arise during the monitoring process.
- **Hint**:
  - Use the `psutil` library in Python to retrieve system information, including CPU usage (`pip install psutil`).
  - Use the `psutil.cpu_percent()` method to get the current CPU usage as a percentage.
- **Expected Output**:

Monitoring CPU usage... Alert! CPU usage exceeds threshold: 85% Alert! CPU usage exceeds threshold: 90% ... (continues until interrupted)



### 3. Configuration File Parser
- **Objective**: Automate configuration management tasks for maintaining consistency and managing infrastructure efficiently.
- **Tasks**:
- Read a configuration file (sample provided).
- Extract specific key-value pairs from the configuration file.
- Store the extracted information in a data structure (e.g., dictionary or list).
- Handle errors gracefully in case the configuration file is not found or cannot be read.
- Save the output file data as JSON in the database.
- Create a GET request to fetch this information.
- **Sample Configuration File**:
```ini
[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080
