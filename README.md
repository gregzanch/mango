# Mango Project

## Step 1

Use `django-admin startproject mango` to start a new django app.
Run `python3 manage.py runserver` to start the server and make sure everything works as expected.

## Step 2

Now we want to create a new `app` called `mangos`. 
> **NOTE**: `mangos` is the name of the app that holds the views, models, templates etc.
> `mango` is the name of base application that holds project level configuration. 

In order to do this we use `python3 manage.py startapp mangos`

## Step 3

### Database setup

First we have to migrate our models. Running `python3 manage.py migrate` will migrate our models to our database.
This means that Django will create database tables for admins, users and other things.
The result of this will be a `db.sqlite3` file at the root of our project.

### Making our own data models

We want to create our own database information about mangos, So lets make a `Mango` model.
The mango will have a `name`, a `rating`, `country` of origin, and its `created` and `updated` date.

Because different mangos can come from the same country, we'll make another model called `Country`.
The `Country` model will have a `name` and `abbreviation` field.

Now we'll run `python3 manage.py makemigrations` to generate the database models,
then we'll run `python3 manage.py migrate` again to add the relevant tables.

### Adding some data from the command line

To add some data we will use the command line interface (CLI) that django provides.
Run the command `python3 manage.py shell` to start the session.

You will see this in your console:

```text
Python 3.9.6 (default, Mar 29 2024, 10:51:09) 
[Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
```

#### 1. Import the newly created models

```pycon
>>> from mangos.models import Mango, Country
```

#### 2. Make a new country and save it

```pycon
>>> c = Country(name="India", abbreviation="IN")
>>> c
<Country: India - IN>
>>> c.save()
```

#### 2. Make a new mango and save it

```pycon
>>> m = Mango(name="Alphonso", country=c)
>>> m
<Mango: Alphonso>
>>> m.save()
```

#### 3. Make sure the country and mango are both added

```pycon
>>> Mango.objects.all()
<QuerySet [<Mango: Alphonso>]>

>>> Country.objects.all()
<QuerySet [<Country: India - IN>]>
```

## Step 4 - Admin

### Create a superuser admin account

To create an admin superuser, run `python3 manage.py createsuperuser`.
Enter a desired username, email, and password.

Next, add the two models to our `admin.py` file, and run the server again using `python3 manage.py runserver`.
Navigate to http://localhost:8000/admin/ and log in. Here we can add users and countries and mangos!