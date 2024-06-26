This is a Django project for a hotel booking application. Users can book a room by selecting either a Standard room, VIP room, or Suite room. After booking, the user will receive a unique booking code.

## Prerequisites
Python (>= 3.6)
pip (Python package installer)
MySQL (with a user and database created)

## Installation

1. Setting Up Django
First, you need to install Django. You can do this using pip:

`pip install django`

2. Installing MySQL Client
To use MySQL as your database backend, you need to install mysqlclient:

`pip install mysqlclient`

3. Enabling Lazy Loading with Django Browser Reload
To enable lazy loading in your Django project, you need to install django-browser-reload:

`pip install django-browser-reload`

## Running the Project
To run the Django development server, use the following command:

`python manage.py runserver`

Visit http://localhost:8000 in your web browser to see your hotel booking application in action.

# Booking Functionality

1. Creating a Booking
2. Navigate to the booking page.
3. Select the type of room (Standard, VIP, or Suite).
4. Fill in the necessary details.
5. Submit the booking form.

After submitting the form, you will receive a unique booking code that you can use to reference your booking.
