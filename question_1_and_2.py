class Base(object):

    def __new__(cls, *args, **kwargs):
        print("Create a new instance of Base Class.")
        return super().__new__(cls)

    def __init__(self, name, value, date):
        print("Initialize the new instance of Base Class.")
        self.name = name
        self.value = value
        self.date = date

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, value={self.value}, date={self.date})"

    @classmethod
    def class_method(self):
        pass
    
    def instance_method(self):
        pass

class Derived(Base):
    
    def __init__(self, name, value, date):
        print("Initialize differently from the Base Class.")
        self.name = "derived " + name
        self.value = "derived " + value
        self.date = "derived " + date

    @classmethod
    def class_method(self):
        print("adding some code inside")

    def instance_method(self):
        print("adding some code inside")

def main():

    derived = Base('teste','teste','teste')

    print(derived)
    print(derived.class_method())
    print(derived.instance_method())

if __name__ == "__main__":
    main()
