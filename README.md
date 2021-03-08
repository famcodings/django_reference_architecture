# Django Reference Project Architecture
Architecture which can be used as a template for a new django project

## Getting Started
- Clone repository : `git clone https://github.com/famcodings/django_reference_architecture.git`
- Create and activate virtual environment: `pipenv shell`
- Install dependencies: `pipenv install`
- Copy .env.example in same directory and rename it as ".env" and write database and email credentials in ".env"
- Search and replace project_name with the required name of the project
- Migrate DB : `python manage.py migrate`
- Runserver : `python manage.py runserver`
- Navigate to url: `localhost:8000`

## Features
- Login
- Logout
- SignUp
- Update Profile
- Change Password
- Reset Password