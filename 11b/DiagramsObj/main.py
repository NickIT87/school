import models


def main():
    # має бути реалізована фабрика студентів ->
    user1 = models.Abiturient(
        name="John",
        age=17,
        mail="hi i need for education ... "
    )
    
    print(user1.name)
    print(user1.sendMessage())
    
    # має бути серверна логіка, яка реалізує роботу закладу
    HRdep = models.HRdepartment()
    HRdep.getMessage(message=user1.sendMessage())
    
    user1.get_rate()
    
    print(HRdep.recived_msgs)


if __name__ == '__main__':
    main()
