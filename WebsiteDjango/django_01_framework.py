# framework is essentially a library of reusable modules
# these models provide functionality for common tasks

# 1. first use terminal to download django
# pip install django  # django==2.1 for version if you want to download a special version

# 2. create a django project,
# we need to excute:
# django-admin startproject name .
# (name. means create a package called that name in this one folder)

# it automatically create a name of 'pyshop' package,  and a manage.py, this file is used to control our django

# 3.terminal: python3 manage.py runserver
# we use this manage.py module to manage our django website

# 4. divide app into different small functions

# 5. terminal: python3 manage.py startapp products
# create some files

# 6. introduce the products folders' different name files
# products package we can reuse it!

# 7. go to product part -> go to views, view functions

# summary: every time, we want to create a new app, first go to create a products, and then go to views set your page,
# and then using urls to define, last go to the pyshop urls to map the app.