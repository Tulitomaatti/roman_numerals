from nose.tools import *

from roman_numerals.roman2num import * 
from roman_numerals.num2roman import * 


def setup():
    print "setup..."

def teardown():
    print "test teardown"

def test_basic():
    print "a test ran."

# # Placeholder example test. 
# @with_setup(setup, teardown)
# def test_fooname():
#     a = roman2num.Foo("Bar") 
#     assert_equal(a.name, "Bar")


# Few tests based on wikipedia Roman_numerals 

def test_bruteforce_small():
	for i in xrange(1,5000): 
		assert_equal(i, r2n(n2r(i)))


def test_basics(): 
	inputs = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
	outputs = [1, 5, 10, 50, 100, 500, 1000]

	for rom, num in zip(inputs, outputs):
		assert_equal(r2n(rom), num)

def test_basics2(): 
	inputs = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
	for num in xrange(0, 10):
		assert_equal(n2r(num+1), inputs[num])

def test_rare_forms():
	# These have historical usage. The whole system is not really standardized. 
	inputs = ['IIII', 'VIIII', 'XIIX', 'IIXX', 'IC', 'IIC', 'MDCCCCX', 'MCMX', 'MDCDIII']
	outputs = [4, 9, 18, 18, 99, 98, 1910, 1910, 1903]

	for rom, num in zip(inputs, outputs):
		assert_equal(r2n(rom), num)