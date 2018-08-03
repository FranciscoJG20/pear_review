# Pear Review Code (PRC)

## Description:

A tool that allows developers to share and review their code. Developers can create an "issue" and other developers can comment on them. Questions are specific to one's code (e.g. how to refactor or make more dry) and users can choose which “pear” reviews their code. It’s a great way to build relationships with developers and a budding opportunity to seek / become a mentor.

## Technologies used:

Python, Django, PostgreSQL, Github, Bootstrap, Heroku

## Installing and running app locally:

1.  Fork and clone this repository
2.  Create and activate a virtual environment (make sure you have Python and Django installed)

    `pip3 install virtualenv`
    `virtualenv .env -p python3`
    `source .env/bin/activate`

3.  Install project requirements

    `pip install -r requirements.txt`

4.  Migrate the database

    `python manage.py makemigrations`
    `python manage.py migrate`

5.  Run the server

    `python manage.py runserver`

6.  Open your browser and navigate to localhost://8000

## Unsolved Issues:

I would like to extend the user model so that users can sign up and update their profile. Additionally, it would be great to implement a many-to-many relationship between users so they could add each other as "pears."

## User Stories

Jay just finished a coding bootcamp and he’s eager to land his first job. He knows that he can continue to work on past projects to make his portfolio stronger. He’s looking for feedback on his code from another developer.

Carla is a self-taught developer, and is currently learning a new programming language. She has questions that are specific to her code that wouldn’t make sense parsing and posting individually in another forum. She she would love to pair up with another developer who could guide her as she continues to learn.

Maseeh has several years of experience under his belt and feels confident teaching others. He’s seeking an opportunity to mentor a junior developer who could improve their code.
