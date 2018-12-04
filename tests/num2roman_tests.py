from nose.tools import *

from romanum.num2roman import *


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

def test_basics():
    inputs = [1, 5, 10, 50, 100, 500, 1000]
    outputs = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    for num, rom in zip(inputs, outputs):
        assert_equal(smallnum2r(num), rom)
        assert_equal(n2r(num), rom)


def test_basics2():
    outputs = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    for num in xrange(0, 10):
        assert_equal(smallnum2r(num + 1), outputs[num])
        assert_equal(n2r(num + 1), outputs[num])


def test_basics3():
    inputs = [1351, 2587, 3254, 666, 4999]
    outputs = ['MCCCLI', 'MMDLXXXVII', 'MMMCCLIV', 'DCLXVI', 'MMMMCMXCIX']

    for num, rom in zip(inputs, outputs):
        assert_equal(smallnum2r(num), rom)
        assert_equal(n2r(num), rom)

def test_zero():
    assert_equal(n2r(0), 'nulla')


def test_negative1():
    outputs = ['-I', '-II', '-III', '-IV', '-V', '-VI', '-VII', '-VIII', '-IX', '-X']
    for num in xrange(0, 10):
        assert_equal(n2r(-num - 1), outputs[num])

def test_negative2():
    inputs = [-1351, -2587, -3254, -666, -4999]
    outputs = ['-MCCCLI', '-MMDLXXXVII', '-MMMCCLIV', '-DCLXVI', '-MMMMCMXCIX']

    for num, rom in zip(inputs, outputs):
        assert_equal(n2r(num), rom)