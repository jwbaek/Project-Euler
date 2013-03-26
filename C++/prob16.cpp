#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

void doubleNum(vector<int> & num)
{
	int carryOver = 0;
	for (int i = 0; i < num.size(); i++)
	{
		int doubled = num.at(i)*2 + carryOver;
		if (doubled >= 10)
		{
			doubled -= 10;
			carryOver = 1;
			if (i == num.size()-1)
			{
				num.push_back(0);
			}
		}
		else
		{
			carryOver = 0;
		}
		num[i] = doubled;
	}
}

void prob16()
{
	vector<int> num;
	num.push_back(1);
	for (int exp = 0; exp < 1000 ; exp++)
	{
		doubleNum(num);
	}
	int sum = 0;
	for (int i = 0; i < num.size(); i++)
	{
		cout << num.at(i);
		sum += num.at(i);
	}
	cout << endl << "sum of digits is " << sum << endl;
}
