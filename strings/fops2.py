# конструкція №1
# open file for reading data
with open("data.txt", "r") as f:
    temp = f.read() # temp file data

print(temp)
print(type(temp), len(temp))
# конструкція № 2
# открыть файл
f = open('data.txt', 'r+')
# for line in f:
#     print(line)
f.write("new data string\n second data")

f.close()

# конструкція з зберігання Строки у форматі JSON
# import json
# with open('test.json', encoding='utf-8') as json_file1:
#     q_base = json.load(json_file1)
#     y = json.dumps(json_file1)

# print(q_base)
# print(type(q_base))
# print(y, type(y))