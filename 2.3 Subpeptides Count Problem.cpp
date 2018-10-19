#include <iostream>
using namespace std;
long int SubpeptidesCount(long int length) {
	return length*(length - 1);
}
int main(){
	long int length;
	cin >> length;
	cout << SubpeptidesCount(length);
	return 0;
}
