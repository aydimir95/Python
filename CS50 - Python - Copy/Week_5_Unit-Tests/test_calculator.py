# this program tests the square function from calculator.py

from calculator import square


def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("ERROR: 2 squared was not 4")
    if square(3) != 9:
        print("ERROR: 3 squared was not 9")

if __name__ == "__main__":
    main()



# assert - allows you to assert that something is true

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9

if __name__ == "__main__":
    main()



# AssertionError - how do we catch this error? try and except



def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")


if __name__ == "__main__":
    main()



# it would be nice not to write 30 lines of code to test 2 lines of function

# pytest - third party program, that automates the testing of your code so long you write your code, you don't have to write as many lines of code. There is other program, 
# like unit testing - testing individual functions in your code


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0




# pip install pytest 
# docs.pytest.org

# main, no conditionals, no prints, non of that bs

# To summarize, I need to create a function that I will be testing, then I'm creating a test file, I "import" the function "from", define the test, assert the desired outcome and run the "pytest 'file name'" - that will test my file.


def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negatie():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

# you can make separate files for different tests


# test str

import pytest

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")



