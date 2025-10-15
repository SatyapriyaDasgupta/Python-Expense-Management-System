# 💰 Expense Management System

The **Expense Management System** is a lightweight full-stack application for tracking, managing, and analyzing expenses.
It uses a **Streamlit frontend**, a **FastAPI backend**, and a **MySQL database**.

This README explains how to run the application directly from the extracted zip file.



## Prerequisites

Before running the app, ensure you have:

- **Python 3.10+** installed
- **MySQL server** installed and running
- `pip` installed (Python package manager)



## Setup Instructions

### 1. Extract the zip file
Extract the contents of the provided zip file to a folder on your computer, e.g., `ExpenseManagementSystem`.

### 2. Install Python dependencies
Open a terminal or command prompt, navigate to the extracted folder, and run:
```bash
pip install -r requirements.txt
````

### 3. Import the provided database

The zip file contains a SQL file with the database (`database/expense_management_db.sql`).

To import it into MySQL:
1. Open a terminal or command prompt.
2. Run the following command (replace `<username>` with your MySQL user):

```bash
mysql -u <username> -p < database/expense_db.sql
```

3. Enter your MySQL password when prompted.

This will create the database and populate it with all tables and sample data.

> **Note:** If you prefer, you can also open MySQL Workbench import the SQL file through the GUI.

### 4. Update database credentials

Open `backend/db_helper.py` and update the connection settings if necessary:

```python
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_USER = "your_mysql_user"
DB_PASSWORD = "your_mysql_password"
DB_NAME = "expense_db"
```



### 5. Start the FastAPI backend

```bash
uvicorn backend.server:app --reload
```

* Backend will run at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
  
* API documentation available at:
  * Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  * ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

> Make sure the backend is running before starting the frontend.

### 6. Start the Streamlit frontend

```bash
streamlit run frontend/app.py
```

* Streamlit will open in your browser at: [http://localhost:8501](http://localhost:8501)



## Common Issues & Troubleshooting

**1. MySQL connection errors**

* Ensure MySQL server is running.
* Verify username, password, host, and port.
* Grant necessary privileges to your user:

```sql
GRANT ALL PRIVILEGES ON expense_db.* TO 'username'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```

**2. Missing Python packages**

* Make sure dependencies are installed using:

```bash
pip install -r requirements.txt
```

**3. Streamlit cannot connect to backend**

* Confirm the backend is running on `127.0.0.1:8000`.
* If using a different host or port, update the API URL in `frontend/app.py`.

**4. Port conflicts**

* Default Streamlit port: 8501
* Default FastAPI port: 8000
* To change Streamlit port:

```bash
streamlit run frontend/app.py --server.port 8502
```


## Notes

* The backend must be running before starting the frontend.
* Keep database credentials secure and do not share them.
* Python 3.10+ is required.



## Author

**Satyapriya Dasgupta**
[GitHub Profile](https://github.com/SatyapriyaDasgupta)



## Acknowledgements

Built with Streamlit and FastAPI. Thanks to the open-source community for libraries and examples that made this project possible.

