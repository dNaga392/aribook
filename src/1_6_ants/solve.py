# -*- coding: utf-8 -*-
# 問題 Ants (POJ No.1852)
# 長さLcmの竿の上をn匹のアリが毎秒1cmのスピードで歩いています。
# アリが竿の端に到達すると竿の下に落ちていきます。
# また、竿の上は狭くてすれ違えないので、二匹のアリが出会うと、
# それぞれ反対を向いて戻っていきます。各アリについて、
# 現在の竿の左端からの距離x(i)はわかりますが、どちらの方向を
# 向いているのかはわかりません。すべてのアリが竿から落ちるまで
# にかかる最小の時間と最大の時間をそれぞれ求めなさい。
#
# 制約
#  1 <= L <= 10^6
#  1 <= n <= 10^6
#  1 <= x(i) <= L


def __is_valid_fall_ants_time_inputs(L: int, n: int, x: tuple) -> bool:
    if L < 3 or 10 ** 6 < L:
        return False
    if n < 3 or 10 ** 6 < n:
        return False
    if n != len(x):
        return False
    for xi in x:
        if xi < 1 or L < xi:
            return False
    return True


def calc_fall_ants_max_time(L: int, n: int, x: tuple) -> int:
    if not __is_valid_fall_ants_time_inputs(L, n, x):
        return -1
    max_time = 0
    for xi in x:
        xi_max_time = max(xi, L-xi)
        max_time = max(max_time, xi_max_time)
    return max_time


def calc_fall_ants_min_time(L: int, n: int, x: tuple) -> int:
    if not __is_valid_fall_ants_time_inputs(L, n, x):
        return -1
    min_time = 0
    for xi in x:
        xi_min_time = min(xi, L-xi)
        min_time = max(min_time, xi_min_time)
    return min_time


if __name__ == "__main__":
    assert calc_fall_ants_min_time(10, 3, (2, 6, 7)) == 4, "case min error"
    assert calc_fall_ants_max_time(10, 3, (2, 6, 7)) == 8, "case max error"
