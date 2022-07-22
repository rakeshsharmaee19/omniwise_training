# We are in the modules1 module
def print_name(name):
    """
    This function does not return anything.
    It will just print your name.
    """
    print("Hello! {}, You are in modules1 module.".format(name))


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

## this is dictionary in module
power = {
    1 : 1,
    2 : 4,
    3 : 9,
    4 : 16,
    5 : 25,
    6 : 36,
    7 : 49,
    8 : 64,
    9 : 81,
    10 : 100
}

## this is list in module
alphabets = ['a','b','c','d','e','f','g','h']
