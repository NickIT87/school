# пошук елементів в таблицях
table1 = [
    #0  1  2
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9]  # 2
]

# функція яка здійснює пошук елемента в таблиці
def search_element(table: list, element):
    row_index = None      #  індекс рядка знаходження елемента в таблиці
    column_index = None   #  індекс стовбчика знаходження елемента в таблиці

    for row in table:
        if element in row:
            row_index = table.index(row)
            column_index = row.index(element)

    print(
        f"елемент: {element} знаходиться у -  рядок:{row_index}, стовпчик:{column_index}"
    )


search_element(table=table1, element=7)