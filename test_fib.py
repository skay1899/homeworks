#contents of test_fib.py
#function to perform unit test
from fib import fib

def test_unit():
	assert fib(2) == 1 and fib(5) == 5 and fib(12) == 144
