#include<iostream>
#include<string>
using namespace std;


int main(){
	string input, reverse;
	cin >> input;
	int length = input.length();
	reverse.resize(length);
	for (int i = 0; i < length; i++){
		switch (input[i]){
		case 'A':
			reverse[length - i - 1] = 'T';
			break;
		case 'T':
			reverse[length - i - 1] = 'A';
			break;
		case 'C':
			reverse[length - i - 1] = 'G';
			break;
		case 'G':
			reverse[length - i - 1] = 'C';
			break;
		}
	}
	cout << reverse;
	return 0;
}
