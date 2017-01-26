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


def is_winnable_kujibiki_bruteforce(n: int, m: int, k: tuple) -> bool:
    if not __is_valid_inputs(n, m, k):
        return False
    for i in range(n):
        for j in range(n):
            for p in range(n):
                for q in range(n):
                    if k[i] + k[j] + k[p] + k[q] == m:
                        return True
    return False


def is_winnable_kujibiki(n: int, m: int, k: tuple) -> bool:
    return is_winnable_kujibiki_bruteforce(n, m, k)


def show_winnable_kujibiki(n: int, m: int, k: tuple) -> None:
    if is_winnable_kujibiki(n, m, k):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    assert is_winnable_kujibiki(3, 10, (1, 3, 5)) == True, "case 1 error"
    assert is_winnable_kujibiki(3,  9, (1, 3, 5)) == False, "case 2 error"
    show_winnable_kujibiki(3, 10, (1, 3, 5))
    show_winnable_kujibiki(3,  9, (1, 3, 5))
