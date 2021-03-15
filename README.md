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

## Documentation
Below are the list of endpoints and what each endpoint does

### Register User 
- https://mmogo-assessment.herokuapp.com/auth/users/
- - send a POST request  to register a new user, here is a sample request data:
```json
    {
        "username": "test",
        "email": "test@test.com",
        "password": "Compl!c@ted"
    }
```
- - sample response:
```json
    {
        "username": "test",
        "email": "test@test.com"
    }
```
- - on successful registeration a user is sent a link via mail to activate the account.

### Activate User 
- https://mmogo-assessment.herokuapp.com/auth/users/activation/
- - NOTE: the `uid` and `token` are  embedded in the url sent to the user's mail for activation.
- - -  the url looks like this https://mmogo-frontend.vercel.app/user/activate/confirm/MjU/ajjzio-37af2b8fa556999dd3ff38fc420eab2e where `MjU` is the `uid` and `ajjzio-37af2b8fa556999dd3ff38fc420eab2e` is the `token`
- - send a POST request  to activate user, here is a sample request data:
```json
    {
        "uid": "MjU",
        "token": "ajjzio-37af2b8fa556999dd3ff38fc420eab2e",
     }
```

### Login 
- https://mmogo-assessment.herokuapp.com/auth/token/login/
- - send a POST request to login, here is a sample request data:
```json
    {
        "email": "test@test.com",
        "password": "Compl!c@ted"
    }
```
- - the endpoint returns a token which will be used for authentiation
```json
    {
        "auth_token": "bBgsduol7p8238ddchdcuou8ds7sdc7"
    }
```
### Reset User Password 
- https://mmogo-assessment.herokuapp.com/auth/users/reset_password/
- - send a POST request to receive a link to reset password, here is a sample request data:
```json
    {
        "email": "test@test.com"
    }
```
### Confirm Password Reset 
- https://mmogo-assessment.herokuapp.com/auth/users/reset_password_confirm/
- -  NOTE: the `uid` and `token` are in embedded in the url sent to the user's mail for password reset.
- - - the url looks like this https://mmogo-frontend.vercel.app/password/reset/confirm/GuY/wxttty-2w5f2b8fa556999dd3ff38fc4f7k8 where `GuY` is the `uid` and `wxttty-2w5f2b8fa556999dd3ff38fc4f7k8` is the `token`
- - send a POST request to set new password, here is a sample request data:
```json
    {
        "uid": "GuY",
        "token" : "wxttty-2w5f2b8fa556999dd3ff38fc4f7k8 ",
        "new_password": "Stre$$ed!"
    }
```
### Get User Details 
- https://mmogo-assessment.herokuapp.com/auth/users/me/
- - requires authentication add this to the request header(Same applies for all  endpoints below):
```json
    Authorization: "Token <user token>"
```
- - send a GET request to get users info. Below is an example response:
```json
    {
        "username": "test",
        "email": "test@test.com" 
    }
```

### List Companies 
- https://mmogo-assessment.herokuapp.com/api/companies/
- - remember to add Authentication to headers.
- - send a GET request to  return  list of companies. Below is an example response:
```json
  [
    {
        "id": 1,
        "name": "Github" ,
        "address": "World Wide Web",
        "phone_no": "+14483449034"
    },
    {
        "id": 2,
        "name": "GitLab" ,
        "address": "World Wide Web",
        "phone_no": "+14483449034"
    }
   ]
```
### Add Favorite 
- https://mmogo-assessment.herokuapp.com/api/fav/<:id>
-  - remember to add Authentication to headers.
- - send a POST request to add a company as favorite

### List Favorites 
- https://mmogo-assessment.herokuapp.com/api/favorites/
- - remember to add Authentication to headers.
- - send a GET request to return list of companies a user has as favorites. Below is an example response:
```json
  [
    {
        "id": 1 ,
        "company" : {
            "id": 2,
            "name": "GitLab" ,
            "address": "World Wide Web",
            "phone_no": "+14483449034"
        },
    }
   ]
```

### Delete Favorite 
- https://mmogo-assessment.herokuapp.com/api/fav/<:id>
- - remember to add Authentication to headers.
- - send a DELETE request to delete a company from favorites
