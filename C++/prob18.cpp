#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <ctime>
using namespace std;

int max(int a, int b)
{
	if (a > b)
		return a;
	return b;
}

int prob18recurse(int row, int col, vector< vector <int> > & pyramid, vector< vector <int> > & memP)
{
	// if memoized
	if (memP.at(row).at(col) != -1)
		return memP.at(row).at(col);

	int curr = pyramid.at(row).at(col);
	if (row == pyramid.size()-1)
	{
		return curr;
	}
	int length =  max(curr + prob18recurse(row+1, col, pyramid, memP), curr + prob18recurse(row+1, col+1, pyramid, memP));
	memP[row][col] = length; // remember length for next time
	return length;
}

void prob18()
{
	vector< vector <int> > pyramid;
	vector< vector <int> > memoPyr;
	ifstream file("prob67_pyramid.txt");
	int line = 1;
	while (!file.eof())
	{
		vector<int> newRow;
		vector<int> rowMem;
		for (int i = 0; i < line; i++)
		{
			int newNum;
			file >> newNum;
			//cout << newNum;
			newRow.push_back(newNum);
			rowMem.push_back(-1);
		}
		pyramid.push_back(newRow);
		memoPyr.push_back(rowMem);
		line++;
	}
	
	// pyramid contains the pyramid
	time_t start = time(NULL);
	int longest = prob18recurse(0,0, pyramid, memoPyr);
	time_t end = time(NULL);
	cout << "longest path is " << longest << endl;
	cout << "time took " << end-start << endl;
}


