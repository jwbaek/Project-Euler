/*
PROBLEM 14

The following iterative sequence is defined for the set of positive long unsigned integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

long unsigned int Collatz(int start, int table[])
{
	long unsigned int nextNum = start;
    long unsigned int count=1;
    while (nextNum != 1)
	{
		if (nextNum%2 == 0)
			nextNum /= 2;
		else
			nextNum = 3*nextNum + 1;
		if (nextNum < 1000000)
			table[nextNum] = 1;
		count++;
	}
    return count;
}

long unsigned int prob14()
{
	cerr << "hey" ;
	int table[999999]; // filled with 0
	int longestSoFar = 999999;
	long unsigned int longestLength = Collatz(999999, table);
	for (int i = 999998; i >= 1 ; i--)
	{
		if (table[i] != 1)
		{
			long unsigned int currLength = Collatz(i, table);
			if (currLength > longestLength)
			{
				longestSoFar = i;
				longestLength = currLength;
			}
		}
	}
	cout << longestSoFar << endl;
	return longestSoFar;
}


