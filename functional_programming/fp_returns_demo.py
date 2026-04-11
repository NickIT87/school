#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Демо основных функциональных конструкций из библиотеки returns:
- Maybe (Some / Nothing)
- Result (Success / Failure)
- map vs bind
- flow (pipeline)
- safe (обработка исключений)
- alt (работа с ошибками)
- value_or
- pointfree стиль
"""

from returns.maybe import Maybe, Some, Nothing
from returns.result import Result, Success, Failure, safe
from returns.pipeline import flow, is_successful
from returns.pointfree import bind, map_


# =========================
# 1. Maybe (Option)
# =========================
def find_user(user_id: int) -> Maybe[str]:
    return Some("Nick") if user_id == 1 else Nothing


def demo_maybe():
    print("\n=== Maybe ===")
    result = find_user(1).map(str.upper)
    print("Some:", result)  # Some('NICK')

    result_none = find_user(2).map(str.upper)
    print("Nothing:", result_none)  # Nothing


# =========================
# 2. Result (Either)
# =========================
def safe_div(x: float) -> Result[float, str]:
    return Failure("division by zero") if x == 0 else Success(10 / x)


def demo_result():
    print("\n=== Result ===")
    print(Success(2).bind(safe_div))  # Success(5.0)
    print(Success(0).bind(safe_div))  # Failure


# =========================
# 3. map vs bind
# =========================
def f(x: int) -> int:
    return x + 1


def g(x: int) -> Result[int, str]:
    return Success(x * 2)


def demo_map_bind():
    print("\n=== map vs bind ===")
    print(Success(1).map(f))   # Success(2)
    print(Success(1).bind(g))  # Success(2)


# =========================
# 4. flow (pipeline)
# =========================
def inc(x: int) -> Result[int, str]:
    return Success(x + 1)


def double(x: int) -> Result[int, str]:
    return Success(x * 2)


def demo_flow():
    print("\n=== flow ===")
    result = flow(
        1,
        Success,
        bind(inc),
        bind(double),
    )
    print(result)  # Success(4)


# =========================
# 5. safe (try/except → Result)
# =========================
@safe
def risky(x: int) -> float:
    return 10 / x


def demo_safe():
    print("\n=== safe ===")
    print(risky(2))  # Success
    print(risky(0))  # Failure


# =========================
# 6. alt (обработка ошибки)
# =========================
def demo_alt():
    print("\n=== alt ===")
    result = Failure("error").alt(lambda e: f"ERROR: {e}")
    print(result)  # Failure('ERROR: error')


# =========================
# 7. value_or (дефолт)
# =========================
def demo_value_or():
    print("\n=== value_or ===")
    print(Nothing.value_or(0))  # 0


# =========================
# 8. pointfree стиль
# =========================
def demo_pointfree():
    print("\n=== pointfree ===")
    result = map_(lambda x: x + 1)(Success(1))
    print(result)  # Success(2)


# =========================
# 9. Реальный pipeline
# =========================
@safe
def parse(x: str) -> int:
    return int(x)


def half(x: int) -> Result[float, str]:
    return Success(x / 2)


def demo_real_pipeline():
    print("\n=== real pipeline ===")
    result = flow(
        "10",
        parse,
        bind(half),
    )
    print(result)  # Success(5.0)


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    demo_maybe()
    demo_result()
    demo_map_bind()
    demo_flow()
    demo_safe()
    demo_alt()
    demo_value_or()
    demo_pointfree()
    demo_real_pipeline()