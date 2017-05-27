/*
 問題1.6　三角形
 n本の棒があります。棒iの長さはa(i)です。あなたはそれらの棒から
 3本を選んでできるだけ周長の長い三角形を作ろうと考えています。
 最大の周長を求めなさい。ただし、三角形が作れない際には0を答えとしなさい。

 制約
  3 <= n <= 100
  1 <= a(i) <= 10^6
 */
#include "solve.h"
#include <vector>
#include <algorithm>

int calc_max_perimeter(int n, std::vector<int> a)
{
    if (n < 3 || 100 < n)
    {
        return 0;
    }
    for (int ai : a)
    {
        if (ai < 1 || 1000000 < ai)
        {
            return 0;
        }
    }
    if (n != (int)a.size())
    {
        return 0;
    }
    std::sort(a.begin(), a.end(), std::greater<int>()); // 降順(5,4,3,...)
    for (int i = 0; i < (int)a.size()-2; ++i)
    {
        if (a[i] < a[i+1] + a[i+2])
        {
            return a[i] + a[i+1] + a[i+2];
        }
    }

    return 0;
}
