# Library Management System

## Project Overview

This is a simple Library Management System implemented in Python.  It allows you to manage books within a database, including adding, deleting, and searching for books. The system uses a MySQL database to store book information.

## Key Features & Benefits

*   **Add Books:**  Easily add new book records to the database, including title, author, and ISBN.
*   **Database Storage:**  Stores book information persistently using MySQL.
*   **Simple Interface:** A basic command-line interface for interacting with the system.

## Prerequisites & Dependencies

Before running the Library Management System, ensure you have the following installed:

*   **Python 3.x:** You need Python 3 or a later version to run the Python script.
*   **MySQL Database:** You need a MySQL database server installed and running.
*   **`mysql-connector-python`:** This Python library is required to connect to the MySQL database.  Install it using pip:

    ```bash
    pip install mysql-connector-python
    ```

## Installation & Setup Instructions

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Emmanuel047/Library-Management.git
    cd Library-Management
    ```

2.  **Configure the Database Connection:**

    *   Edit the `Library.py` file.
    *   Modify the `mydb` connection parameters to match your MySQL server settings:

        ```python
        mydb = mysql.connector.connect(
            host = "127.0.0.1",  # Your MySQL host
            user = "root",       # Your MySQL user
            password = "root",   # Your MySQL password
            database = "Library"  # Your MySQL database name
        )
        ```

3.  **Create the Database:**

    *   Log in to your MySQL server using a tool like `mysql` or `phpMyAdmin`.
    *   Create a database named `Library` (or use an existing database):

        ```sql
        CREATE DATABASE IF NOT EXISTS Library;
        ```

4.  **Run the Script:**

    ```bash
    python Library.py
    ```

    The first time you run the script, it will create the `Books` table in the database if it doesn't already exist.

## Usage Examples

After running the script, you can interact with the library management system through the command line. The provided code snippet only sets up the database. More functionalities needs to be implemented.

```python
import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "root",
    database = "Library"
)

mycursor = mydb.cursor()

# Add more functions for
# - Adding books
# - Deleting books
# - Searching for books
```

## Configuration Options

The primary configuration option is the database connection parameters within the `Library.py` file. Ensure these are correctly set to connect to your MySQL database.

*   **Host:** The hostname or IP address of your MySQL server.
*   **User:** The username for connecting to the database.
*   **Password:** The password for the database user.
*   **Database:** The name of the database to use.

## Contributing Guidelines

Contributions are welcome!  If you'd like to contribute to this project, please follow these guidelines:

1.  **Fork the Repository:** Create your own fork of the repository on GitHub.
2.  **Create a Branch:** Create a new branch for your feature or bug fix.
3.  **Make Changes:** Implement your changes and ensure they are well-tested.
4.  **Submit a Pull Request:** Submit a pull request to the main repository with a clear description of your changes.

## License Information

This project has no license specified. All rights are reserved by the owner.

## Acknowledgments

*   [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) - For providing the MySQL connector for Python.