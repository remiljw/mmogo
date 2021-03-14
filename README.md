# Mmogo Assessment

[![TeleMedicine](https://circleci.com/gh/remiljw/mmogo.svg?style=svg)](https://circleci.com/gh/remiljw/mmogo)

- This is the backend of the Mmogo Assessment. This repo has to be run simultaneously with the frontend at https://github.com/remiljw/mmogo-frontend

## Setup
- Clone this repo on your machine 
- cd into 'mmogo' and create a virtualenv and activate it
- run `pip install -r requirements.txt`
- create a `.env` file at the root of the project and add the needed variables for the database, reference the settings page to know what variables to set.
- In your `.env` file set your DOMAIN to be the running port of the react server. i.e `localhost:3000`, set the SITE_NAME to any of your choice. 
- run `python manage.py migrate`
- run `python manage.py loaddata data.json` to populate the database
- run `python manage.py runserver`
- Hurray! you have the back end set up.
- Visit https://github.com/remiljw/mmogo-frontend to set up the front end.