import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        # Запам'ятовуємо поточний час перед викликом функції
        start_time = time.time()
        # Викликаємо функцію
        result = func(*args, **kwargs)
        # Запам'ятовуємо час після виклику функції
        end_time = time.time()
        # Обчислюємо тривалість виконання
        execution_time = end_time - start_time
        # Виводимо результат та час виконання
        print(f"Результат: {result}")
        print(f"Час виконання: {execution_time} секунд")
        return result
    return wrapper
