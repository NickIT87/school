# інкапсуляція - приховування даних або логіки

# наслідування

# поліморфізм

class Base(object):
    # public
    data: str = "some data"
    # private
    __private_data: str = "private data"

    @staticmethod
    def some_method(x, y):
        return x + y
    
    def __init__(self, data=None) -> None:
        self.__private_data = data

    def __del__(self):
        print("object deleted")
    
    def __str__(self) -> str:
        return "Base object"

    # application programming interface
    def get_data(self):
        return self.__private_data


class Parent(Base):
    b = 6

    def get_data(self):
        return self.b

    def some_case(self, x: str) -> str:
        return x
    
    def some_case(self, y: int) -> int:
        return y


#a = Parent()
#print(a.some_case(12))


from dataclasses import dataclass


@dataclass
class Employee(object):
    # required args
    first_name: str
    second_name: str
    birth: str
    # non required args
    age: int = None


e1 = Employee("John", "Smith", birth="01.10.1990")
print(e1)