# -*- coding: utf-8 -*-
# 
# [部分和問題]
# 整数a(1)、a(2)、…、a(n)が与えられます。その中からいくつか選び、
# その和をちょうどkにすることができるかを判定しなさい。
#
# <!>制約
#  1 <= n <= 20
#  -10^8 <= a(i) <= 10^8
#  -10^8 <= k <= 10^8


def __is_valid_inputs(n: int, a: tuple, k: int) -> bool:
    if n < 1 or 20 < n:
        return False
    if len(a) != n:
        return False
    for ai in a:
        if 10 ** 8 < abs(ai):
            return False
    if 10 ** 8 < abs(k):
        return False
    return True


def __dfs(i: int, sum: int, a: tuple, k: int) -> bool:
    if i == len(a):
        return sum == k
    if __dfs(i + 1, sum, a, k):
        return True
    if __dfs(i + 1, sum + a[i], a, k):
        return True
    return False


def __contains_subset_sum_dfs(n: int, a: tuple, k: int) -> bool:
    return __dfs(0, 0, a, k)


def contains_subset_sum(n: int, a: tuple, k: int) -> bool:
    if not __is_valid_inputs(n, a, k):
        return False
    return __contains_subset_sum_dfs(n, a, k)


if __name__ == "__main__":
    assert contains_subset_sum(4, (1, 2, 4, 7), 13) == True, "case true"
    assert contains_subset_sum(4, (1, 2, 4, 7), 15) == False, "case false"
