# Lead Select

Lead Select is a Django-based web application used for voting for student related posts (prefcts, dorm monitors, church wardens, e.t.c)

## Project Structure

    lead_select/
    ├── core/                # Main Django app
    ├── lead_select/         # Project configuration
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3           # SQLite database
    ├── manage.py            # Django management script
    ├── requirements.txt     # Python dependencies
    └── README.md

## Requirements

-   Python 3.10+
-   pip

## Setup Instructions

1.  **Clone the repository**

    ``` bash
    git clone https://github.com/SibusiZW/lead-select.git
    cd lead_select
    ```

2.  **Create and activate a virtual environment**

    ``` bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**

    ``` bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations**

    ``` bash
    python manage.py migrate
    ```

5.  **Run the development server**

    ``` bash
    python manage.py runserver
    ```

6.  Open your browser and visit:

        http://127.0.0.1:8000/

## Common Commands

-   Create superuser:

    ``` bash
    python manage.py createsuperuser
    ```

-   Run tests:

    ``` bash
    python manage.py test
    ```

## Environment Variables (Optional)

For production, configure: - `DEBUG` - `SECRET_KEY` - `ALLOWED_HOSTS`

## License

This project is provided as-is for development and learning purposes.
