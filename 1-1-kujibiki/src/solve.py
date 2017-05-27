# 問題 くじびき
# あなたの友人は次のようなゲームをあなたに仕掛けてきました。数字の書かれたn枚の紙切れが袋に入って
# います。あなたはこの袋から紙切れを取り出し、数字を見て袋に戻すということを4回行い、 4回の紙切れ
# の数字の和がmになっていればあなたの勝ち、そうでなければ友人の勝ちとなります。あなたはこのゲーム
# に何度か挑戦しましたが、一度も勝つことができませんでした。怒ったあなたは袋を破り、すべての紙切れを
# 取り出して本当に勝つ可能性があるのかを調べることにしました。紙切れに書かれている数字がk1,k2,...,kn
# であったとき、和がmになる取り出し方が存在するかどうかを計算し、存在するならYes, 存在しないなら
# ばNoと出力するプログラムを作成してください。
#
# 制約
#  1 <= n <= 50
#  1 <= m <= 10^8
#  0 <= k(i) <= 10^8


from bisect import bisect_left 


def __is_valid_inputs(n: int, m: int, k: tuple) -> bool:
    if n < 3 or 50 < n:
        return False
    if m < 3 or 10 ** 8 < m:
        return False
    if n != len(k):
        return False
    for ki in k:
        if ki < 0 or 10 ** 8 < ki:
            return False
    return True


def is_winnable_bf(n: int, m: int, k: tuple) -> bool:
    """bruteforce: 総当り4重ループ"""
    if not __is_valid_inputs(n, m, k):
        return False
    for i in range(n):
        for j in range(n):
            for p in range(n):
                for q in range(n):
                    if k[i] + k[j] + k[p] + k[q] == m:
                        return True
    return False


def is_winnable_in(n: int, m: int, k: tuple) -> bool:
    """in list: in-探索"""
    if not __is_valid_inputs(n, m, k):
        return False
    kk = [k[i] + k[j] for j in range(n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if m - k[i] - k[j] in kk:
                return True
    return False


def __binary_search(x: int, kk: list) -> bool:
    l = 0
    r = len(kk)
    while r - l >= 1:
        i = (l + r) // 2
        if kk[i] == x:
            return True
        if kk[i] < x:
            l = i + 1
        else:
            r = i
    return False


def is_winnable_bs(n: int, m: int, k: tuple) -> bool:
    """binary search: 二分探索（自前実装）"""
    if not __is_valid_inputs(n, m, k):
        return False
    kk = [k[i] + k[j] for j in range(n) for i in range(n)]
    kk.sort()
    for i in range(n):
        for j in range(n):
            if __binary_search(m - k[i] - k[j], kk):
                return True
    return False


def __binary_search_bis(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, x, lo, hi)
    return pos != hi and a[pos] == x


def is_winnable_bis(n: int, m: int, k: tuple) -> bool:
    """binary search: 二分探索（bisect）"""
    if not __is_valid_inputs(n, m, k):
        return False
    kk = [k[i] + k[j] for j in range(n) for i in range(n)]
    kk.sort()
    for i in range(n):
        for j in range(n):
            if __binary_search_bis(kk, m - k[i] - k[j]):
                return True
    return False


def is_winnable(n: int, m: int, k: tuple) -> bool:
    # 1. 4-loop
    # return is_winnable_bf(n, m, k)
    # 2. in list
    # return is_winnable_in(n, m, k)
    # 3. binary search (self)
    # return is_winnable_bs(n, m, k)
    # 4. binary search (bisect)
    return is_winnable_bis(n, m, k)


def show_winnable(n: int, m: int, k: tuple) -> None:
    print("Yes" if is_winnable(n, m, k) else "No")


if __name__ == "__main__":
    assert is_winnable(3, 10, (1, 3, 5)) == True, "case 1 error"
    assert is_winnable(3,  9, (1, 3, 5)) == False, "case 2 error"
    show_winnable(3, 10, (1, 3, 5))
    show_winnable(3,  9, (1, 3, 5))
