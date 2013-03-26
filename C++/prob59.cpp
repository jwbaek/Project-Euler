#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <ctime>
#include <algorithm>
#include <sstream>
#include <map>
using namespace std;

/*
	XOR decryption

	had help with http://www.mathblog.dk/project-euler-59-xor-encryption/
*/


vector<int> &split(const string &s, char delim, vector<int> &elems) {
    stringstream ss(s);
    string item;
    while(getline(ss, item, delim)) {
		int item_int = atoi(item.c_str());
        elems.push_back(item_int);
    }
    return elems;
}

vector<int> decrypt_msg(vector<int> msg, vector<int> keys)
{
	vector<int> encryptedMessage;
	int sum = 0;
	for (int i = 0; i < msg.size(); i++) {
		int decrypted = msg.at(i) ^ keys.at(i%keys.size());
		encryptedMessage.push_back(decrypted);
		sum += decrypted;
    }
	cout << "sum is " << sum << endl;
    return encryptedMessage;
}

void prob59()
{
	ifstream file("prob59.txt");
	string wholeFile;
	file >> wholeFile;
	vector<int> values;
	char delim = ',';

	values = split(wholeFile, delim, values);	// vector of ints
	int total_count = values.size();			// total number of ints

	map<int,int> freq1;							// thee different maps 
	map<int,int> freq2;							// since there are three keys
	map<int,int> freq3;
	int i = 0;
	for (vector<int>::iterator it=values.begin(); it!=values.end(); ++it)
	{
		int mycount = std::count (values.begin(), values.end(), *it);
		map<int, int>* currmap;

		if(i%3 == 0)
			currmap = &freq1;
		else if(i%3 == 1)
			currmap = &freq2;
		else
			currmap = &freq3;

		// not in map already
		if ( currmap->find(*it) == currmap->end() ) 
		{
			(*currmap)[*it] = 1;
		}
		else
		{
			(*currmap)[*it]++;
		}
		i++;
	}
	for (map<int,int>::iterator it=freq1.begin(); it!=freq1.end(); ++it)
	{
		cout << "key: " << it->first << " value: " << it->second << endl;
	}
	cout << endl << endl;
	for (map<int,int>::iterator it=freq2.begin(); it!=freq2.end(); ++it)
	{
		cout << "key: " << it->first << " value: " << it->second << endl;
	}
	cout << endl << endl;
	for (map<int,int>::iterator it=freq3.begin(); it!=freq3.end(); ++it)
	{
		cout << "key: " << it->first << " value: " << it->second << endl;
	}

	// find the keys by finding the numbers with the largest value
	// and matching it with the 'space' character, ascii 32
	// numbers with largest values: 71, 79, 68 respectively
	// 32 ^ 71 = 103
	// 32 ^ 79 = 111
	// 32 ^ 68 = 100
	vector<int> keys;
	keys.push_back(103);
	keys.push_back(111);
	keys.push_back(100);

	vector<int> decrypted = decrypt_msg(values, keys);

}


int main()
{
	prob59();
	int first = 32;
	int second = 68;
	int a = first ^ second;
	cout << "a is " << a << endl;
	system("Pause");
	return 0;
}