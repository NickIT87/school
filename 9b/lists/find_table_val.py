# пошук елементів в таблицях
table1 = [
    #0  1  2
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9]  # 2
]

# функція яка здійснює пошук елемента в таблиці
def search_element(table: list, element):
    row = None      #  індекс рядка знаходження елемента в таблиці
    column = None   #  індекс стовбчика знаходження елемента в таблиці

    for i in table:
        if element in i:
            row = table.index(i)
            column = i.index(element)

    print(f"елемент: {element} знаходиться у -  рядок: {row}, стовпчик: {column}")


search_element(table=table1, element=7)