# Alfax

this is the first Version of Alfax made by Love in Django.


## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ git clone git@gitlab.com:jupidev-code/alfax.ir.git
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt

# Create Super user And Migrations.

$ cd alfax.ir/
$ python manage.py createsuperuser 
$ python manage.py makemigrations
$ python manage.py migrate

# Finally Run Project.

$ python manage.py runserver <port>
```

## Features

* Manage and Modify your Company Contact.
* Manage and Modify your Company Accounting.
* Manage and Modify Construction Company Accounting.
* Split settings in two files. `settings_custom.py` for specific environment settings (localhost, production, etc). `projectname/settings.py` for core settings.
* Simple logging setup ready for production envs.

## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.


## TODO List
    [✔] set up Jalali Calender for Project
    [✔] Look up for Blog and Landing Page Template and Add To Project
    [ ] Add item 'Add Contact' to Contact 


    [✔] Add Landing Page Models
    [✔] Add Resume Page Models

    [ ] Set Up Resume Page Html With View
    [ ] Set up New Landing Page 

    [✔] Add Model Managers to Blog
    [ ] Add Model Managers to Land(prject)

    [✔] add a Landing as a new application
    [✔] add a Dashboard as a new application
    [✔] add a blog as a new application
    [ ] add karfarmaonline as a new application