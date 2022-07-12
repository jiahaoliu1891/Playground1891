import time
class MyClass:
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        time.sleep(5)
        return "hi my name is: {}".format(self.name)

# instantiates MyClass and calls a method on the object
def myclass_function():
    param1 = MyClass("foo")
    # returns "hi my name is: foo"
    return param1.sayhi()