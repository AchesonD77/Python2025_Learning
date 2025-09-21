# 1. packages in python, it is basically another way to organize our code, maybe there are more than thounds modules
# so, the best way is to find the related modules, so package is a container for multiple modules.

# way to create - new - add a new directory --- then we must add a new python file in that new directory.
# a special convention in Python
# __init__.py
# 2. the best way is doing: create - new python package, pycharm will automatically create for us.(__init__.py)

# 3. how to import a package
# two ways
# we must import package first, then module, then function
import directory_1_py_36_ecommerce.shipping
directory_1_py_36_ecommerce.shipping.calc_shipping()

# another way, we can append it at the end (here are two ways)
# from directory_1_py_36_ecommerce.shipping import calc_shipping #, calc_tax
from directory_1_py_36_ecommerce import shipping
shipping.calc_shipping()