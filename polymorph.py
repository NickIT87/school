class Parent:
    __mark = "test_mark"

    def __test(self):
        return self.__mark

    def value(self, a: str) -> str:
        return a

    def value(self, a: int) -> int:
        return a
    

a = Parent()

print(a.value(12), type(a.value(12)))
print(a.value("hello"), type(a.value("hello")))