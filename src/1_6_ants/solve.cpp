#include "solve.h"
#include <vector>
/*
 問題 Ants (POJ No.1852)
 長さLcmの竿の上をn匹のアリが毎秒1cmのスピードで歩いています。
 アリが竿の端に到達すると竿の下に落ちていきます。
 また、竿の上は狭くてすれ違えないので、二匹のアリが出会うと、
 それぞれ反対を向いて戻っていきます。各アリについて、
 現在の竿の左端からの距離x(i)はわかりますが、どちらの方向を
 向いているのかはわかりません。すべてのアリが竿から落ちるまで
 にかかる最小の時間と最大の時間をそれぞれ求めなさい。

 制約
  1 <= L <= 10^6
  1 <= n <= 10^6
  1 <= x(i) <= L
 */

int calc_fall_ants_max_time(int L, int n, const std::vector<int> & x)
{
	return -1;
}
int calc_fall_ants_min_time(int L, int n, const std::vector<int> & x)
{
	return -1;
}
