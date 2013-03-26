#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <ctime>
#include <algorithm>
using namespace std;

bool myfunction (string name1, string name2) 
{
	return name1.compare(name2) < 0;
}

void prob22()
{
	ifstream file("prob22_names.txt");
	string allNames;
	file >> allNames;
	//cout << allNames;
	char* p = new char[allNames.length()+1];
	strcpy( p, allNames.c_str() ); 
	char * pch;

	vector<string> listOfNames;
	pch = strtok (p,",\"");
	int j = 0;
	while (pch != NULL)
    {
		string name(pch);
		listOfNames.push_back(name);
		if (j < 50)
			cout << name << endl;
		pch = strtok (NULL, ",\"");
		j++;
    }
	sort (listOfNames.begin(), listOfNames.end());
	// now listOfNames has the list of names sorted
	long long int totalScore = 0;
	int pos = 1;
	for (vector<string>::iterator it=listOfNames.begin(); it!=listOfNames.end(); ++it)
	{
		string name = *it;
		int value = 0;
		for (size_t i=0; i < name.length(); i++)
		{
			value += (int)name.at(i) - 'A' + 1;
		}
		//cout << "Value for " << name << " is " << value << endl;
		totalScore += value*pos;
		if (name.compare("COLIN") == 0)
			cout << "Value for " << name << " is " << value << " and pos is " << pos << " and score is " << value*pos << endl;
		pos++;
	}
	cout << "Total score is " << totalScore << endl;
}

// 870 885 382

