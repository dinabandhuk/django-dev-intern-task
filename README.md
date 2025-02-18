# django-dev-intern-task
Django based website with DRF REST API. Student entry system.

## Installation
- Clone this repository
```bash
git clone https://github.com/dinabandhuk/django-dev-intern-task.git
```
- Navigate into the repository
```bash
cd django-dev-intern-task
```

- Create a virtual environment and activate it
```bash
python -m venv .venv
```
```bash
source .venv/bin/activate
```
- Install the required packages  
```bash
pip install requirements.txt
```
- We will use sqlite3 as the database; which comes default with django

## Run the webapp

- Navigate to the webapp directory and make necessary migrations
```bash
cd studentEntry
```
```bash
python manage.py makemigrations
```
- Create superuser to access admin panel
```bash
python manage.py createsuperuser
```
- run the server on localhost:8025
```bash
python manage.py runserver 8025
```

## Endpoints
The application will be available at 
```bash
127.0.0.1:8025
```
- admin/ - admin panel


### API Endpoints

### 1. List All Students
- **URL**: `/api/students/`
- **Method**: `GET`
- **Description**: Retrieve a list of all students.
- **Response**: Returns a JSON array containing details of all students.

**Example Response:**
```json
  {
    "id": 1,
    "name": "John Doe",
    "grade": "A",
    "major": "Computer Science",
    "address": "123 Main St"
  }
```



### 2. Retreive Student details
- **URL**: `/api/students/{id}`
- **Method**: `GET`
- **Description**: Retrieve details of a specific student by ID.
- **Response**: Returns a JSON array containing details of student.

**Example Request:**
```bash
GET /api/students/1/
```
**Example Response:**
```json
  {
    "id": 1,
    "name": "John Doe",
    "grade": "A",
    "major": "Computer Science",
    "address": "123 Main St"
  }
```
### 3. Update Student information
- **URL**: `/api/students/{id}`
- **Method**: `PATCH`
- **Description**: Update student details
- **Request**: JSON object with fields to be updated

**Example Request:**
```json
  {
    "id": 1,
    "name": "John Doe update",
    "grade": "A",
    "major": "Computer Science",
    "address": "123 Main St updated"
  }
```
**Example Response:**
```json
  {
    "id": 1,
    "name": "John Doe update",
    "grade": "A",
    "major": "Computer Science",
    "address": "123 Main St updated"
  }
```
### 4. delete student
- **URL**: `/api/students/{id}`
- **Method**: `DELETE`
- **Description**: Delete student with given id
- **Example Request**
```bash
DELETE /api/students/1/
```
- **Response**: 
```json
{
  "message": "Student with ID 1 deleted successfully."
}
```