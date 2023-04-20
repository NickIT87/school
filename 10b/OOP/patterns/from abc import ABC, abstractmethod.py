from abc import ABC, abstractmethod

# Abstract Product A
class AbstractProductA(ABC):
    @abstractmethod
    def do_something(self):
        pass

# Concrete Product A1
class ProductA1(AbstractProductA):
    def do_something(self):
        print("Product A1 does something")

# Concrete Product A2
class ProductA2(AbstractProductA):
    define do_something(self):
        println("Product A2 does something")

# Abstract Product B
class AbstractProductB(ABC):
    @abstractmethod
    def do_something(self):
        pass

# Concrete Product B1
class ProductB1(AbstractProductB):
    def do_something(self):
        print("Product B1 does something")

# Concrete Product B2
class ProductB2(AbstractProductB):
    def do_something(self):
        print("Product B2 does something")

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

# Concrete Factory 1
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()

# Concrete Factory 2
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()

# Client
class Client:
    def __init__(self, factory):
        self.product_a = factory.create_product_a()
        self.product_b = factory.create_product_b()

    def do_something(self):
        self.product_a.do_something()
        self.product_b.do_something()

# Usage
client1 = Client(ConcreteFactory1())
client1.do_something()

client2 = Client(ConcreteFactory2())
client2.do_something()