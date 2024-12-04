# Registration Task
# Registration App

### Prerequisites
1. Python 3.x installed
2. PostgreSQL installed and running

### Setup Instructions
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd registration
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Configure PostgreSQL:
    - Create a database in PostgreSQL.
    - Update `DATABASES` settings in `settings.py`.

4. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the server:
    ```bash
    python manage.py runserver
    ```

6. Access the API at:
    - Create: `POST /create/`
    - Read: `GET /`
    - Update: `PUT /update/<id>/`
    - Delete: `DELETE /delete/<id>/`
