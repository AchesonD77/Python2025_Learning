# 1. we find there is a db.sqlite3
# we use it to store our data, dajang support all the database

# 2. go to website use da SQLite

# 3. create code to automatically create our database table

# 5. we go to pyshop(main package) to find settings.py, and then find 'INSTALLED_APPS'
# we type: 'products.apps.ProductsConfig' (that class we saw in step5)

# 4. before 5, we go to products(created package) to find apps.py, and then go 4

# 6. go to terminal: python3 manage.py makemigrations

# 7. type terminal: python3 manage.py migrate

# 8. next time if we create a new model in models.py, we need to create a new migration, and do one more migrate