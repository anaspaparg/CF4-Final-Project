# Social Media Site

Social Media Site is a social media Django web application for creating, updating and deleting users, creating posts and updating posts for authenticated users, as well as uploading user profile images. The full-stack application is written in Python. For the client side, Django template is used, which includes HTML, CSS, and Javascript. For the server side, Django framework is used for the models and the logic. Finally sqlite is used for database and CRUD operations.

## Table of Contents
- [Features]
- [Installation]
- [Usage]
- [File Structure]


## Features
- User authentication and registration
- Update user's information
- Posting and deleting content
- Updating content for authenticated users
- Uploading user profile images

## Installation
1. Clone the repository:
   https://github.com/anaspaparg/angular-introduction.git
2. Create a virtual environment: python -m venv "virtual environment name"
3. Install dependencies from requirements.txt: pip install -r requirements.txt
4. Apply migrations: python manage.py migrate

## Usage
1. Run the development server:python manage.py runserver
2. Access the application in your browser at 'http://localhost:8000'

## File Structure
- media: User images.
- post:
    static:
      css: CSS files for styling.
      javascript: JavaScript files for client-side functionality.
    templates: HTML templates.
    forms.py: Posts forms.
    models.py: Posts models.
    urls.py: Url paths
    views.py: View functions.
- social_media_site: Django project settings.
- users: User-related functionality.
    forms.py: Registration user forms
    models.py: User image model
    urls.py: Url paths
