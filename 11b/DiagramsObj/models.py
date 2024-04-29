from abc import abstractmethod


class Person:
    name: str = "noname"
    age: int = 0
    

class Student(Person):
    grades: list = []
    
    
class Abiturient(Person):
    mail: str = "get my education ... "
    result_rate: float = 0
    
    def __init__(self, name, age, mail="dumb", result_rate=0) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.mail = mail
        self.result_rate = result_rate
    
    def sendMessage(self):
        return self.mail
    
    def get_rate(self):
        self.result_rate = GeneralDepartment.getRate()
        print(self.result_rate)
        
    
class Professor(Person):
    listOfStudents: list


class HRdepartment:
    
    recived_msgs: list = []
    result_rate: float = 0
    
    def getMessage(self, message):
        print("getMessage: ", message)
        self.recived_msgs.append(message)

    
class GeneralDepartment():
    """main object"""
    @abstractmethod
    def getRate():
        import random
        return random.randint(1, 100)
    
