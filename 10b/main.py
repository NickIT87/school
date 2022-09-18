import second
from mod1.module_one import send_message


stud1 = second.Student("Vasyan", "Student")

def main():
    print("start programming", stud1.name)
    print(send_message("call message"))

# точка входу
if __name__ == '__main__':
    main()