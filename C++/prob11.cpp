#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;


int prob11()
{
	cout << "hi" << endl;
	ifstream gridtext("prob11_grid.txt");
	vector< vector<int> > grid; // stores grid

	// read in grid.txt into 2d vector grid
	for (int i = 0; i < 20; i++)
	{
		vector<int> newRow;
		for (int j = 0; j < 20; j++)
		{
			int newNum;
			gridtext >> newNum;
			newRow.push_back(newNum);
		}
		grid.push_back(newRow);
	}
	// now check for largest prod
	int largestProd = 0;
	for (int i = 0; i < 20; i++)
	{
		for (int j = 0; j < 20; j++)
		{
			if (grid[i][j] != 0)
			{
				int currprod;
				// check down
				if (i <= 16)
				{
					currprod = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j];
					largestProd = currprod > largestProd ? currprod : largestProd;
					// check diag right
					if (j <= 16)
					{
						currprod = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3];
						largestProd = currprod > largestProd ? currprod : largestProd;
					}
					// check diag left
					if (j >= 3)
					{
						currprod = grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3];
						largestProd = currprod > largestProd ? currprod : largestProd;
					}

				}
				// check right
				if (j <= 16)
				{
					currprod = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3];
						largestProd = currprod > largestProd ? currprod : largestProd;
				}
			}
		}
	}
	cout << "largest is " << largestProd << endl;

	system("Pause");
	return 0;
}