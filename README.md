# Boilerplate  FastAPI Project

## Project Overview

This project provides a RESTful API for user relation. It is built using **FastAPI**, database by using **PostgreSQL**, ORM as **SQLalchemy** and includes database migrations via **Alembic**. The project structure ensures modularity, scalability, and ease of maintenance.

Here attached whole project is done by following asynhronous manner and synchronoys approach. By using the `AsyncSession`, `AsyncEngine`, and `asyncpg` and **Async SQLalchemy** and `Session`, `create_engine` and **SQLalchemy**.

---

## Directory Structure


### 1. `alembic` Directory
Handles database schema migrations.

- **`versions`**: Contains migration scripts.
- **`env.py`**: Configuration for Alembic migrations.

### 2. `src` Directory
It contains all the subdirectory such as `api`, `core`, `dao`, `dto`, `exceptions` and `utils`

### 3. `api` Directory
Contains scripts and API for fetching and displaying data from the database.

- **`common_endpoints.py`**: Contains all common endpoints of api.
- **`healthcheck.py`**: check the health status.
- **`user.py`**: All api related CRUD for the user .
- **`version.py`**: API for checking the version of project.

### 4. `core` Directory
Contains the configuration of the application.

- **`config.py`**: Stores configuration settings such as environment variables.

### 5. `dao` Directory
Handles database interactions, models, and configuration.

- **`database.py`**: Manages database sessions and connections.
- **`models/user.py`**: Defines the database models for user.
- **`users.py`**: Contains data access object which contain all database related operation for user.

### 6. `dto` Directory
Contains data validation and serialization schemas by using pydantic models.

- **`user.py`**: Handles user-related data transfer object.
- **`version.py`**: Handles user-related data transfer object.


### 7. `exception` Directory
Handles custom exceptions used throughout the project.

- **`exceptions.py`**: Defines application-specific exceptions.

### 8. `service` Directory
Handles service layer and converter function for Database object to DTO and DTO to Database object.

- **`converter.py`**: Handles the db to dto and dto to db converter function script for the API.
- **`user_service.py`**: Handles the user service layer script.

### 9. `utils` Directory
Handles custom exceptions used throughout the project.

- **`constants.py`**: Defines all your constants 
- **`utils.py`**: Defines application-specific repetable code in this file to avoid redundant code.

### 10. `tests` Directory
Handles database schema migrations.

- **`test_users.py`**: Testing script for the API by using pytest module.

---

## Getting Started

### Prerequisites
- Python 3.12.2
- PostgreSQL or a compatible database
- Alembic for database migrations
- Uvicorn to run the FastAPI application

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fastapi-boilerplate.git
   cd fastapi-boilerplate

2. Set up a virtual environment:
   ```bash
   python3.12 -m venv myenv
   source myenv/bin/activate  # On Windows, use myenv\Scripts\activate

3. Install poetry:
   ```bash
   poetry install 

4. Configure environment variables and set up the your `.env` file by adding necessary inputs to the variables in `.env` file :
   ```bash
   cp .env.template .env

Update the `.env` file in database configuration details.

5. Apply database migrations:
   ```bash
   alembic upgrade head

6. Start the application:
   ```bash
   uvicorn main:app --reload
 
7. For formatting the python file use black
   ```bash
   pip install black
   black src # To format the entire src folder

---

- Setting up environment variables in the `alembic.ini` file `db.py`

| Key     | Value |
| ----------- | ----------- |
| SQLALCHEMY_DATABASE_URL   | postgresql://user:password@host:port/db|
| sqlalchemy.url   | postgresql+psycopg2://user:pass@localhost/dbname|


### Setting up the database

* Install PostgreSQL and create your user and database

* Change this line in ` db.py ` to 

``` 
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{settings.YOUR_DATABASE_USERNAME}:{settings.YOUR_DATABASE_PASSWORD}@{settings.YOUR_DATABASE_HOST}:{settings.YOUR_DATABASE_PORT}/{settings.YOUR_DATABASE_NAME}"

```

# Usage

- Access the API at `http://localhost:<port>`.
- Explore the available CRUD operations for users.

## Project Structure
```
   .
   ├── myenv
   ├── alembic
   │   ├── versions
   │   │   └── 2025_01_31_0943-7f4e8bd3822c_create_user_tabel.py
   │   │   └── 2025_01_31_1056-e8bcbe6fb338_add_column_status.py
   │   └── env.py
   │   └── README.md
   │   └── script.py.mako
   ├── src
   │   ├── api
   │   │   ├── common_endpoints.py
   │   │   ├── healthcheck.py
   │   │   ├── user.py
   │   │   ├── version.py
   │   ├── core
   │   │   └── config.py
   │   ├── dao
   │   │   └── models
   │   │       └── user.py
   │   │   ├── db.py
   │   │   ├── users.py
   │   ├── dto
   │   │   ├── user.py
   │   │   ├── version.py
   │   ├── exceptions
   │   │   └── user.py
   │   ├── service
   │   │   └── converter.py
   │   │   ├── user_service.py
   │   ├── utils
   │   │   └── constants.py
   │   │   ├── utils.py
   │   └── version.py
   ├── tests
   │   ├── __init__.py
   │   ├── test_users.py
   ├── .env.template
   ├── .gitignore
   ├── alembic.ini.template
   ├── main.py
   ├── poetry.lock
   ├── pyproject.toml
   └── README.md
```

### Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. Ensure your changes include proper tests and documentation.