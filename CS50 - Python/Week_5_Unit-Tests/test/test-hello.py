from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"


# create a file "__init__.py" inside the test folder with you test files and python will treat that folder as a package - which is a module organized inside of the folder

# Here is what I learned today: assert. AssertionError. pytest. Packages. __init__.py.

