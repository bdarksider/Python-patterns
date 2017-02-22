class Car(object):
    def __init__(self, name):
        self.name = name 

print(Car("this")) # prints object location 

class Car(object):
    def __init__(self, name):
        self.name = name 

    def __enter__(self):
        return self.name 

    def __exit__(self, Type, value, traceback):
        pass 

with Car("ferrari") as obj:
    print(obj) # prints ferrari 
