# открыть файл
f = open('data.txt', 'r+')

# переменная строкового типа для хранения текста, полученного из файла
text: str = ""

# цикл записи каждой строки открытого файла в переменную "текст"
for line in f:
    print(line)
    text += line

# сортировка символов строки - возвращает массив символов
sorted_string = sorted(text)

# вывод информации
print(text)
print(type(sorted_string))
print(sorted_string)

# запись в файл полученного текста в обратном порядке
f.write(text[::-1])

# закрыть файл
f.close()