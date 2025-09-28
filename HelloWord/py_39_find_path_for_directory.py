# two path to import packages
from pathlib import Path

# Absolute path - start from disk - /user/local/
# Relative path - start from now repository


path = Path("directory_1_py_36_ecommerce")
# find if we have the directory/package, return boolean value
print(path.exists())
# create new directory
# path = Path("for_test")
# print(path.mkdir())
# delete the directory
# path = Path("for_test")
# print(path.rmdir())

# another way
path = Path("")
for file in path.glob('*.py'): #x.py #x.xls
    print(file)
# generator object

# you can find more packages in PYPI