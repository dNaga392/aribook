/*
 問題 くじびき
 あなたの友人は次のようなゲームをあなたに仕掛けてきました。数字の書かれたn枚の紙切れが袋に入って
 います。あなたはこの袋から紙切れを取り出し、数字を見て袋に戻すということを4回行い、 4回の紙切れ
 の数字の和がmになっていればあなたの勝ち、そうでなければ友人の勝ちとなります。あなたはこのゲーム
 に何度か挑戦しましたが、一度も勝つことができませんでした。怒ったあなたは袋を破り、すべての紙切れを
 取り出して本当に勝つ可能性があるのかを調べることにしました。紙切れに書かれている数字がk1,k2,...,kn
 であったとき、和がmになる取り出し方が存在するかどうかを計算し、存在するならYes, 存在しないなら
 ばNoと出力するプログラムを作成してください。

 制約
  1 <= n <= 50
  1 <= m <= 10^8
  0 <= k(i) <= 10^8
 */
#include "solve.h"

#include <iostream>


bool is_winnable_kujibiki(int n, int m, const std::vector<int> &k)
{
	return false;
}

void show_winnable_kujibiki(int n, int m, const std::vector<int> &k)
{
	if (is_winnable_kujibiki(n, m, k))
	{
		std::cout << "Yes" << std::endl;
		return;
	}
	std::cout << "No" << std::endl;
}

