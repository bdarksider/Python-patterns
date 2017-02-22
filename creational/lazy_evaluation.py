"""lazily-evaluated property pattern in python"""

import functools

class lazy_property(object):

    def __init__(self, function):
        self.function = function
        # relatives is function now!
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


class Person(object):

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        relatives = "Many relatives."
        return relatives


def main():
    Jhon = Person('Jhon', 'Coder')
    print("Name: {0}    Occupation: {1}".format(Jhon.name, Jhon.occupation))
    print("Before we access `relatives`:")
    print(Jhon.__dict__)
    print("Jhon's relatives: {0}".format(Jhon.relatives))
    print("After we've accessed `relatives`:")
    print(Jhon.__dict__)


if __name__ == '__main__':
    main()