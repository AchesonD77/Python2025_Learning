# 2. we use this class HttpResponse to create a Http response and return it to browser or client.
from django.http import HttpResponse
from django.shortcuts import render
# 1. django is a package, shortcuts is a module, and we are importing the render function.


# 3. Create your views here.
def index(request): # main page
    return HttpResponse('Hello World')

def new(request):
    return  HttpResponse("New Products")
# and then we go to map urls point(products)

# 4. (URL) /products -> function index
# uniform resource locator (address)

# 5. go to create a new python file -> urls