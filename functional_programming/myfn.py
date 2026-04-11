# from fn.monads import Either

# def divide_by_2(x):
#     if x == 0:
#         return Either.Left("Деление на ноль!")
#     return Either.Right(x / 2)

# def add_5(x):
#     return Either.Right(x + 5)

# # Цепочка с bind
# result = (
#     Either.Right(10)
#     .bind(divide_by_2)
#     .bind(add_5)
#     .alt(lambda e: f"Обработана ошибка: {e}")  # Обработка ошибки
# )

# print(result)  # Right(10.0)

from returns.result import Result, Success, Failure
from returns.pipeline import is_successful

def divide_by_2(x: float) -> Result[float, str]:
    if x == 0:
        return Failure("Деление на ноль!")
    return Success(x / 2)

def add_5(x: float) -> Result[float, str]:
    return Success(x + 5)

# Цепочка вычислений
result = (
    Success(12)
    .bind(divide_by_2)
    .bind(add_5)
)

# Обработка результата
if is_successful(result):
    print(f"Результат: {result.unwrap()}")
else:
    # unwrap_failure возвращает значение ошибки
    print(f"Ошибка: {result.failure()}")