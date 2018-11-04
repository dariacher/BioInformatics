
#include <iostream>
#include <map>  
#include <string>
using namespace std;

int masses[18] = { 57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186 };



int main() {
	int mass;
	map<int, int32_t> N = { {0,1} };
	cin >> mass;
	for (int i = 57; i <= mass; i++) {
		N[i] = 0;
		for (int j = 0; j < 18; j++) {
			if (N.find(i - masses[j]) != N.end()) {
				N[i] += N[i - masses[j]];
			}
		}
	}

	cout << N[mass];
	return 0;
}
