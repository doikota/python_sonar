import math

# πに定数aの二乗を掛ける関数
def calc_pi(a):
    return a * a * math.pi

# ネイピア数に定数aの二乗を掛ける関数
def calc_e(a):
    return a * a * math.e

if __name__ == "__main__":
    # 実行結果 100の二乗にπを掛けると314.15926535897932になる
    print (calc_pi(100))

    # 実行結果 100の二乗にネイピア数を掛けると271.82818284590452になる
    print(calc_e(100))  
