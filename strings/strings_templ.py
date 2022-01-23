# шаблоны
template = "\t {0}, {1}, {2:.2}"
print(template.format('Student', 'IPMM', 0.567))
print('%s, %d, %.2f \n' % ('spam', 12, 222.455)) 
student = {
    'name': 'Nick',
    'organization': 'IPMM',
    'course': 1
}
print('%(name)s, %(organization)s, %(course)d' % student)

# встроенные шаблоны
import string
t = string.Template('$page: $book')
print(t.substitute({'page': 2, 'book': 'dictionary'}))
print(t.safe_substitute({'page': 2}))

# методы
print('hello'.capitalize())
print('hello'.upper())
print('123'.isdigit())
print('hello'.count('l'))

# поиск
print('lorem ipsum dolor sit amet'.find('ipsum'))
print('lorem ipsum dolor sit amet'.rfind('muspi'))

# регулярные выражения
import re
result = re.findall(
    r'@\w+.\w+', 
    'abc.test@gmail.com, xyz@test.in, first.test@rest.biz'
)
print(result)
