from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str

# Creating an instance of the Person class
person1 = Person(name="Alice", age=30, email="alice@example.com")


class Admin:
    name: str
    age: int
    email: str
    
    def __init__(self, name, age, email) -> None:
        self.name = name
        self.age = age
        self.email = email
        
    def __str__(self) -> str:
        return "Admin object"

# Creating an instance of the Person class
admin1 = Admin(name="Alice", age=30, email="alice@example.com")

print(person1)
print(admin1)

# Accessing attributes of the instance
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
print(person1.email) # Output: alice@example.com
