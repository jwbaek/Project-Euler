#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

// Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
int prob13()
{
	vector<string> strNums;
	int numberOfNums = 100;
	int numberOfDigits = 50;
	ifstream file("prob13_num.txt");
	for (int i = 0; i < numberOfNums; i++)
	{
		string str;
		file >> str;
		strNums.push_back(str);
	}
	vector<int> digits;
	int carryover = 0;
	int sumSoFar = 0;
	for (int digit = numberOfDigits-1; digit >= 0; digit--)
	{
		sumSoFar = carryover;
		carryover = 0;
		for (int num = 0; num < numberOfNums; num++)
		{
			int currDigit = (int) strNums.at(num)[digit] - '0';
			sumSoFar += currDigit;
			while (sumSoFar >= 10)
			{
				sumSoFar -= 10;
				carryover++;
			}
		}
		digits.push_back(sumSoFar);
	}
	cout << "carry over is " << carryover << endl;
	for (int j = digits.size()-1; j >= 0; j--)
	{
		cout << digits[j];
	}
	cout << endl;
	return 0;

}
