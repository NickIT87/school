# def get_score(team_number: int) -> str:
#     match (team_number):
#         case 1 | 2 | 5:
#             return "Spain"
#         case 3 | 7:
#             return "Deutsch"
#         case 4 | 9 | 10:
#             return "England"
#         case 6 | 8:
#             return "Portuguese"
#         case _:
#             return "Undefined"

#print(get_score(int(input("Input team number: "))))

# 1
A = 235.125

def first_task(A):
    # отримаємо цілу частину
    integer_part = int(A)
    # отримаємо дробову частину
    fractional_part = int(str(A).lstrip(str(integer_part) + '.'))
    # виконаємо перетворення в двійковий код
    binary_ip = bin(integer_part)
    binary_fp = bin(fractional_part)
    # виконаємо перевірку
    assert int(binary_ip, 2) == integer_part
    assert int(binary_fp, 2) == fractional_part
    # повернемо відповідь
    return f"{binary_ip}.{binary_fp}"

print(first_task(A))
