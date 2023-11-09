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

def float_to_binary(number: float) -> str:
    # вилучаємо цілу частину
    integer_part = int(number)
    # вилучаємо дробову частину
    fractional_part = number - integer_part
    # конвертуємо цілу частину в бінарне представлення
    binary_integer_part = bin(integer_part).lstrip('0b')
    # конвертуємо дробову частину в бінарну за формулою 
    # 0.125 × 2 = 0.25 (Take the whole number part, which is 0)
    # 0.25 × 2 = 0.5 (Take the whole number part, which is 0)
    # 0.5 × 2 = 1 (Take the whole number part, which is 1)
    binary_fractional_part = ''
    while fractional_part > 0:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional_part += str(bit)
        fractional_part -= bit
    return f"{binary_integer_part}.{binary_fractional_part}"


def binary_to_decimal(binary_string):
    # розділимо рядок бінарного коду на цілу та 
    # дробову частину за символом . якщо це можливо
    parts = binary_string.split('.')
    # перетворимо цілу частину у цілий тип int
    whole_number = int(parts[0], 2)
    # якщо існує дробова частина, сконвертуємо її у число за прикладом:
    # 0 * 2^-1 + 0 * 2^-2 + 1 * 2^-3 = 0 + 0 + 0.125 = 0.125₁₀
    if len(parts) == 2:
        fractional = sum(int(digit) * 2**-(i+1) for i, digit in enumerate(parts[1]))
        return whole_number + fractional
    else:
        return whole_number

# Example usage:
binary_string = float_to_binary(A)
decimal_result = binary_to_decimal(binary_string)
print(binary_string, decimal_result)
