#include <QtTest/QtTest>
#include <vector>
#include <cmath>

#include "../../src/1_6/solve.h"

class Test16 : public QObject
{
	Q_OBJECT
private slots:
	void test_data();
	void test();
};

void Test16::test_data()
{
	QTest::addColumn<int>("n");
	QTest::addColumn<int>("expected");

	// <ex.1>
	// n = 5
	// a = {2, 3, 4, 5, 10}
	// => 12 (selected 3, 4 and 5)
	QTest::newRow("case 1") << 5 << 12;
	// <ex.2>
	// n = 4
	// a = {4, 5, 10, 20}
	// => 0 (no selected)
	QTest::newRow("case 2") << 4 << 0;
}
void Test16::test()
{
	QFETCH(int, n);
	QFETCH(int, expected);

	// bad know-how
	std::vector<int> a;
	if (n==5)
	{
		a.push_back(2);
		a.push_back(3);
		a.push_back(4);
		a.push_back(5);
		a.push_back(10);
	}
	else if (n==4)
	{
		a.push_back(4);
		a.push_back(5);
		a.push_back(10);
		a.push_back(20);
	}
	QCOMPARE(calc_max_perimeter(n, a), expected);
}

QTEST_MAIN(Test16)
#include "test16.moc"
