#include<iostream>
#include<string>
using namespace std;

int main(){
	string pattern, genome;
	int pos = -1, count = 0;
	cin >> pattern;
	cin >> genome;
	while ((pos = genome.find(pattern, pos + 1)) != std::string::npos)
		count++;
	cout << count;

	return 0;
}
