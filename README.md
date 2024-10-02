# Inventory Management System 

A Django-based Inventory Management System
with PostgreSQL as the database backend. This system provides a REST API
for managing items, including CRUD operations, authentication, and
token-based authorization using JWT.

## Features 

- User registration and login with JWT authentication 
- Create, Read, Update, and Delete (CRUD) operations for items 
- PostgreSQL database for storing inventory data 
- Token-based access using Django Rest Framework (DRF) 

## Setup Instructions 

### Step 1: Clone the Repository 

To get started, clone this repository to your local machine:

``` 
git clone https://github.com/krishna-teja18/inventory-management.git
```

Navigate to the project directory:

``` 
cd inventory-management 
```

### Step 2: Set Up the Virtual Environment 
It's recommended to use a virtual environment for managing dependencies. If
you don't have `virtualenv` installed, install it with:

``` 
pip install virtualenv 
```

Now create a virtual environment:

``` 
virtualenv venv 
```

Activate the virtual environment:

- On Windows:

```
venv\Scripts\activate
```

- On macOS/Linux:

```
source venv/bin/activate 
```

### Step 3: Install Dependencies 
Make sure to install all dependencies by running:

```
pip install -r requirements.txt 
```

### Step 4: Configure the Database
1. **PostgreSQL Setup:**

- Install PostgreSQL on your local machine if you haven't already.

- Create a PostgreSQL database:

2. **Update `settings.py`:**

- Open `inventory/settings.py` and update the `DATABASES` section with your
PostgreSQL credentials, adding your password: 
```
DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': 'inventory_db', 
        'USER': 'postgres', 
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost', 
        'PORT': '5432', 
    }
} 
```

### Step 5: Run Database Migrations
Run the following commands to apply the migrations and set up the
database schema:

```
python manage.py migrate 
```

### Step 6: Create a Superuser 
To create an admin user who can log in to the Django admin panel, run the
following command:

```
python manage.py createsuperuser 
```

Follow the prompts to set up a username, email, and password for the superuser.

### Step 7: Run the Development Server 
To run the development server, use the following command:

```
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`` to access the application.

### Step 8: Access the Admin Panel 
To access the Django admin panel, visit:

```
http://127.0.0.1:8000/admin/
``` 

Log in with the superuser credentials you created earlier.

## API Endpoints 

Here are the available API endpoints:

- Register a new user: `POST /api/register/`
- Login: `POST /api/login/` 
- Create an item: `POST /api/items/` 
- Retrieve an item: `GET /api/items/<id>/` 
- Update an item: `PUT /api/items/<id>/`
- Delete an item: `DELETE /api/items/<id>/` 

## Testing the API with Postman 
- Use Postman or another API client to test the available endpoints. 
- Ensure you pass the JWT token in the Authorization header for protected routes. 
- Example for adding a token in Postman:
  
Key: `Authorization` 

Value: `Bearer <your_token_here>`
