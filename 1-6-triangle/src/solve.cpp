/*
 ���1.6�@�O�p�`
 n�{�̖_������܂��B�_i�̒�����a(i)�ł��B���Ȃ��͂����̖_����
 3�{��I��łł��邾�������̒����O�p�`����낤�ƍl���Ă��܂��B
 �ő�̎��������߂Ȃ����B�������A�O�p�`�����Ȃ��ۂɂ�0�𓚂��Ƃ��Ȃ����B

 ����
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
    std::sort(a.begin(), a.end(), std::greater<int>()); // �~��(5,4,3,...)
    for (int i = 0; i < (int)a.size()-2; ++i)
    {
        if (a[i] < a[i+1] + a[i+2])
        {
            return a[i] + a[i+1] + a[i+2];
        }
    }

    return 0;
}
