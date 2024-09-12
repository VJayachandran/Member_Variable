# create a class private variable named pi=3.141
class myClass:
    a = 35;
    def __privMeth(self):
        print("I'm inside class myClass")
    def hello(self):
        print("Private Variable Value: ", myClass.a)

foo = myClass()
foo.hello()
foo.a