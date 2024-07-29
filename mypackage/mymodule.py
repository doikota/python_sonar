"""
This module provides functions for calculating the area of a circle and performing other mathematical operations.
"""
import math

# πに定数aの二乗を掛ける関数
def calc_pi(r: float) -> float:
    """
    Calculates the area of a circle with radius 'r' using the formula: r ** 2 * pi.

    Parameters:
    r (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return r * r * math.pi

# ネイピア数に定数aの二乗を掛ける関数
def calc_e(a: float) -> float:
    """
    Calculates the result multiplying 'a' square and then multiplies to 'e'.

    Parameters:
    a (float): The constant value.

    Returns:
    float: The result of the calculation.
    """
    return a * a * math.e

if __name__ == "__main__":
    # 実行結果 100の二乗にπを掛けると314.15926535897932になる
    print (calc_pi(100))

    # 実行結果 100の二乗にネイピア数を掛けると271.82818284590452になる
    print(calc_e(100))
