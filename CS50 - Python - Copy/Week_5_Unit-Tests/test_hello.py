from hello import hello

def test_hello():
    hello("David") == "hello David" 


def test_default():
    assert hello() == "hello, world" 

def test_argument():
    assert hello("David") == "hello, David" 



def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"


# suppose we have a folder of tests and we would like to organize them pytest supports it. 
