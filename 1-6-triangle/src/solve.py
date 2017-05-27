# -*- coding: utf-8 -*-
# ���1.6�@�O�p�`
# n�{�̖_������܂��B�_i�̒�����a(i)�ł��B���Ȃ��͂����̖_����
# 3�{��I��łł��邾�������̒����O�p�`����낤�ƍl���Ă��܂��B
# �ő�̎��������߂Ȃ����B�������A�O�p�`�����Ȃ��ۂɂ�0�𓚂��Ƃ��Ȃ����B
#
# ����
#  3 <= n <= 100
#  1 <= a(i) <= 10^6
def calc_max_perimeter(n, a):
    if n < 3 or 100 < n:
        return 0
    for ai in a:
        if ai < 1 or 10 ** 6 < ai:
            return 0
    if n != len(a):
        return 0
    a.sort(reverse=True) # �~��(5,4,3,...)
    for i in range(0, len(a)-2):
        if a[i] < a[i+1] + a[i+2]:
            return a[i] + a[i+1] + a[i+2]
    return 0

if __name__ == "__main__":
    assert calc_max_perimeter(5, [2, 3, 4, 5, 10]) == 12, "case1 error"
    assert calc_max_perimeter(4, [4, 5, 10, 20]) == 0, "case2 error"
