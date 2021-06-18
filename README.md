# weekly-voting-system

## Backend

    The system will contain one relational database (PostGres) which provides two endpoints.
    The database will contain two tables, one that stores employees, and another that stores winners.
    An employee has a name(char) and a nickname(char) field.
    A winner has foreign key of an employee and a score(int) field.
    The first endpoint only supports a GET request and will return a list of users.
    The second endpoint will only support a GET request and a POST request. The GET request will return a list of employees and their total score.
    The POST request will increment the score of the chosen employee

## Frontend

    A screen to list all the employees and they total score, ordered by total score, descending.
    A button for each employee that calls the POST command to increment the score

## setup

1. Build the django and postgres image
   `docker-compose build`

During this process I have added a custom command to stop the django running before postgres. its called wait_for_db

2. Make migrations
   `docker-compose run web python manage.py makemigrations voting`
   `docker-compose run web python manage.py migrate voting`
3. Generate 100 fake users
   `sudo docker-compose run web python manage.py seed_users`

To achieve this I wrote a command in the voting app that pulls data from a json file.
