#include "solve.h"
#include <vector>
#include <cmath>
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
  0 <= x(i) <= L
 */

namespace
{
    /** 
     * @brief get max time until all ants fall
     * 
     * @param[in] L : a length of pole
     * @param[in] n : a count of ants
     * @param[in] x : positions of ants
     * 
     * @return a validity of variables
     */
    bool is_valid_fall_ants_time_inputs(int L, int n, const std::vector<int> & x)
    {
        if (L < 1 || 1000000 < L)
        {
            return false;
        }
        if (n < 1 || 1000000 < n)
        {
            return false;
        }
        if ((int)x.size() != n)
        {
            return false;
        }
        for (int xi : x)
        {
            if (xi < 0 || L < xi)
            {
                return false;
            }
        }
        return true;
    }
}

/** 
 * @brief get max time until all ants fall
 * 
 * @param[in] L : a length of pole
 * @param[in] n : a count of ants
 * @param[in] x : positions of ants
 * 
 * @return max time
 */
int calc_fall_ants_max_time(int L, int n, const std::vector<int> & x)
{
    if (is_valid_fall_ants_time_inputs(L, n, x) == false)
    {
        return -1;
    }

    // calc max time
    int max_time = 0;
    for (int xi : x)
    {
		bool was_falled = (xi == 0 || xi == L);
        int xi_max_time = was_falled ? 0 : std::max(xi, L-xi);
        max_time = std::max(max_time, xi_max_time);
    }
    return max_time;
}

/** 
 * @brief get min time until all ants fall
 * 
 * @param[in] L : a length of pole
 * @param[in] n : a count of ants
 * @param[in] x : positions of ants
 * 
 * @return min time
 */
int calc_fall_ants_min_time(int L, int n, const std::vector<int> & x)
{
    // check variables
    if (is_valid_fall_ants_time_inputs(L, n, x) == false)
    {
        return -1;
    }

    // calc min time
    int min_time = 0;
    for (int xi : x)
    {
		bool was_falled = (xi == 0 || xi == L);
        int xi_min_time = was_falled ? 0 : std::min(xi, L-xi);
        min_time = std::max(min_time, xi_min_time);
    }
    return min_time;
}

