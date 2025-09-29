# 1. use package, module, function
from django.urls import path
# 3. from current folder we import views
from . import  views

# 2. default code
urlpatterns = [
    # we mapped the root url to the views function
    path('', views.index), # no () behind index
    # add a new /products/new
    path('new', views.new)
]

# 4. go to pyshop folder, there is a root urls file
