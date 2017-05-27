#include <QtTest/QtTest>
#include "../src/solve.h"


class Test : public QObject
{
    Q_OBJECT
private slots:
    void test_data();
    void test();
};

void Test::test_data()
{
    QTest::addColumn<int>("n");
    QTest::addColumn<int>("m");
    QTest::addColumn<bool>("expected");

    // <ex.1>
    // n = 3
    // m = 10
    // k = {1, 3, 5}
    // => "Yes" (ex: 1, 1, 3 and 5)
    QTest::newRow("case 1") << 3 << 10 << true;
    // <ex.2>
    // n = 3
    // m = 9
    // k = {1, 3, 5}
    // => "No"
    QTest::newRow("case 2") << 3 << 9 << false;
}

void Test::test()
{
    QFETCH(int, n);
    QFETCH(int, m);
    QFETCH(bool, expected);

    // bad know-how
    std::vector<int> k;
    k.push_back(1);
    k.push_back(3);
    k.push_back(5);

    QCOMPARE(is_winnable_kujibiki(n, m, k), expected);
}

QTEST_MAIN(Test)
#include "test.moc"
