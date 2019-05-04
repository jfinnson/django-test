# How is My Team?
A simple Django application to allow daily checkins and monitoring of your teams happiness.

## Requirements

Create a simple Django application that:

1. Allows a user to login.
2. Once per day, users are asked for the happiness level from 1 (Unhappy) to 3 (Neutral) to 5 (Very Happy)
3. After they have entered their happiness level or upon any return visit, shows a statistics page.
4. The statistics page anonymously displays the number of people at each level and the average happiness of the team.
5. New users can be added via the Django admin.
6. Bonus: SaaS! Users can belong to teams and only their teams stats are shown.

## Guidelines

* You MUST include installation instructions so that it can be run locally be other developers.
* You MUST document any applications or external packages you use.
* You SHOULD be following Django best practices.
* You SHOULD take as little or as long as you need (but don't overdo it). You will not be evaluated on time to complete.
* You SHOULD ask questions if anything specified here is not clear in any way.
* You SHOULD incrementally commit to this repository along the way.

## Instructions

1. Fork this github repository using your personal github account.
2. Create your solution. Test it. Test it again to be sure. Commit it and push to your personal repo.
3. Submit a PR (pull request) back to this repository indicating your solution is ready for review.

## Evaluation Criteria

You will be evaluated with the following in mind:

* Does the solution satisfy the five (or 6) requirements?
* Does the solution run locally based on the provided instructions?
* Does the solution make good use of tools/frameworks/libraries/APIs?
* Does the implementation follow established best practices (design patterns, language usage, code formatting, etc..)?


################################
# jfinnson's readme



## SETUP

Following are required for running locally:
* virtualenv
* python 3.X (3.5.2 was used initially)
* pip

OR

* pycharm :)

THEN
1. Create migrations `python manage.py makemigrations`
2. Run migrations `python manage.py migrate`
3. Create a super user `python manage.py createsuperuser --email admin@example.com --username admin`
4. Create any desired users via Django Admin `python manage.py runserver` -> `http://127.0.0.1:8000/admin/`

## TO RUN
* RUN `python manage.py runserver` 
* OPEN `http://localhost:8000/`

# Assumptions Made:
* Users can only enter their happiness once per day
* Happiness level can be only one of the following integers: 1,2,3,4,5 (as opposed to 1,3,5)

## Design Rational
* Happiness could have been tracked on the user. I opted for a happiness history table because I thought it would be a 
better design choice for the long term.
* Used a new model for teams rather than reusing groups because I did not want to overload that model for a different 
use case.
* Decided on many-to-one relationship within team model because I did not want to add a field to users. 
Also creating a new user model at this point would have required a migration of data which I wanted to avoid for the 
scope of this take home. However, this does make the join a bit annoying in Django filters.

## Future Changes
It is not the intent of this code to be ready for production, because of this a few things are intentionally left 
out for the interest of time.
* Proper CSS library (like bootstrap)
* Proper Javascript Framework like react
* Add error display to forms
* Unit and integration testing
* Exhaustive RESTful API for happiness history
* Use of a more scalable database like postgres
* Libraries and code required to deploy to AWS (following a tutorial like this 
https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/)
* Addition of registration, forgot password, and other account views and UI links
* Refactor form approach to possibly follow more of the Django REST best practices (after I learn them)
* More validation and defensive coding! But I want this to be relatively slim for now.
