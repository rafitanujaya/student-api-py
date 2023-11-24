# Student API

## Overview

This Flask application provides a simple API for managing student records. It includes CRUD (Create, Read, Update, Delete) operations for handling student information.

## Technologies Used

- Flask
- Swagger
- SQLAlchemy
- MySQL (as an example database)

## Setup

### Prerequisites

Before running the application, make sure you have the following installed:

- Python 3
- pip (Python package installer)
- MySQL (or any other database of your choice)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/rafitanujaya/student-api-py.git
    cd Milestones
    ```

2. **Install venv:**

    ```bash
    python3 -m venv venv
    ```

    actived venv

    ```bash
    source venv/bin/activate    // linux or mac os
    .\venv\Scripts\activate     // windows
    ```

    deadactived venv
    ```bash
    deactivate  
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**

    Create a `.env` file in the project root and add the following:

    ```bash
    SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://username:password@localhost:3306/student_database
    ```

### Usage

Run the application:

```bash
python3 app.py
# Student Management API

## Overview

Visit [http://localhost:5000/api/ui/](http://localhost:5000/api/ui/) in your browser to access the Swagger UI and explore the API.

## API Endpoints

### Retrieve All Students

**Endpoint:**

- `GET /api/student`

**Description:**

Retrieve a list of all students.

### Create a Student

**Endpoint:**

- `POST /api/student`

**Description:**

Create a new student.

### Get Student by ID

**Endpoint:**

- `GET /api/student/{Id}`

**Description:**

Retrieve details of a specific student by ID.

### Update Student by ID

**Endpoint:**

- `PUT /api/student/{Id}`

**Description:**

Update information for a specific student by ID.

### Delete Student by ID

**Endpoint:**

- `DELETE /api/student/{Id}`

**Description:**

Delete a specific student by ID.

## Swagger Documentation

Explore and interact with the API using the Swagger documentation.

Visit [http://localhost:5000/api/ui/](http://localhost:5000/api/ui/) in your browser.

## Contributing

Feel free to contribute to the development of this project. Follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License.
