# Backend-Intern-Task
# Google Calendar Integration with Django

This project demonstrates the integration of Google Calendar with a Django REST API using the OAuth2 mechanism. It allows users to authorize the application to access their Google Calendar and retrieve a list of events.

## Prerequisites

Before running this project, ensure you have the following prerequisites:

- Python 3.8 or above installed on your machine
- Django 4.2.1 or above
- Google API credentials (client ID, client secret, and redirect URI) for OAuth2 authentication with the Google Calendar API

## Installation

1. Clone the repository to your local machine:  
   git clone https://github.com/your-username/google-calendar-django.git

2. Navigate to the project directory:
   cd google-calendar-django

3. Install the required dependencies:
   pip install -r requirements.txt

4. Set up the project:

- Open the `Assignment/settings.py` file.
- Use `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, and `GOOGLE_REDIRECT_URI` credentials obtained from the Google API Console.

5. Run database migrations:
   python manage.py migrate
   
6. Start the development server:
   python manage.py runserver

7. Access the application in your web browser at `http://localhost:8000/`.

## Usage

- To initiate the OAuth2 flow and prompt the user for their credentials, visit `http://localhost:8000/rest/v1/calendar/init/`.
- After successful authentication, the user will be redirected to `http://localhost:8000/rest/v1/calendar/redirect/` with an authorization code.
- The application will exchange the authorization code for an access token and retrieve a list of events from the user's Google Calendar.
- The events will be displayed as a JSON response.







