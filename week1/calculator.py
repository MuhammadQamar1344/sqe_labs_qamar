# week1/calculator.py
def add(a, b):
   return a + b
def subtract(a, b):
   return a -b
# week1/test_calculator.py
from calculator import add, subtract
def test_add_positive():
   assert add(2, 3) == 5
def test_subtract():
   assert subtract(10, 4) == 6
# Run from terminal:
# cd week1
# pytest test_calculator.py -v