# 2. we use this class HttpResponse to create a Http response and return it to browser or client.
from django.http import HttpResponse
# 1. django is a package, shortcuts is a module, and we are importing the render function.
from django.shortcuts import render
# a. in views change the text into db variables.
from .models import Product


# 3. Create your views here.
def index(request): # main page
    # lots of method to get value, like all(), get(), filter(), save()
    # save in a variable value
    products = Product.objects.all()
    # return HttpResponse('Hello World')
    # change return to get HTML
    return render(request, 'index.html',
                  # dictionary that contains the detail values.
                  {'products': products})


def new(request):
    return  HttpResponse("New Products")
# and then we go to map urls point(products)

# 4. (URL) /products -> function index
# uniform resource locator (address)

# 5. go to create a new python file -> urls