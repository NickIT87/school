# флаг 'r' означает прочитать из файла
with open('test.txt', 'r') as f:
    old_data = f.read()

new_data = old_data.replace('Lorem', 'World')

# флаг 'w' означает записать в файл
with open ('test.txt', 'w') as f:
    f.write(new_data)