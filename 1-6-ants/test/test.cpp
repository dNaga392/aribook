#include <QtTest/QtTest>
#include <vector>
#include "../src/solve.h"


class Test : public QObject
{
    Q_OBJECT
private slots:
    void test();
    void test_stdvector2();
    void test_array();
};

void Test::test()
{
    // <ex>
    // L = 10
    // n = 3
    // x = {2, 6, 7}
    // => min : 4 (left, right, right)
    // => max : 8 (right, right, right)
    int L = 10;
    int n = 3;
    std::vector<int> x;
    x.push_back(2);
    x.push_back(6);
    x.push_back(7);

    int min = 4;
    int max = 8;
    QCOMPARE(calc_fall_ants_min_time(L, n, x), min);
    QCOMPARE(calc_fall_ants_max_time(L, n, x), max);
}

void Test::test_stdvector2()
{
    // <ex>
    // L = 10
    // n = 3
    // x = {0, 6, 10}
    // => min : 4
    // => max : 6
    int L = 10;
    int n = 3;
    std::vector<int> x;
    x.push_back(0);
    x.push_back(6);
    x.push_back(10);

    int min = 4;
    int max = 6;
    QCOMPARE(calc_fall_ants_min_time(L, n, x), min);
    QCOMPARE(calc_fall_ants_max_time(L, n, x), max);
}

void Test::test_array()
{
    // <ex>
    // L = 10
    // n = 3
    // x = {2, 6, 7}
    // => min : 4 (left, right, right)
    // => max : 8 (right, right, right)
    int L = 10;
    int n = 3;
    int x[3] = {2, 6, 7};

    int min = 4;
    int max = 8;
    QCOMPARE(calc_fall_ants_min_time(L, n, x), min);
    QCOMPARE(calc_fall_ants_max_time(L, n, x), max);
}

QTEST_MAIN(Test)
#include "test.moc"
