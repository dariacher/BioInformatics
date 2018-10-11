#include <iostream>
#include<string>
using namespace std;

int main() {
   string dna, pattern;
    cin>> pattern;
    cin >> dna;
    int count = 0;
    for (int i = 0; i < dna.size() - pattern.size(); i++) {
        if (dna.substr(i, pattern.size()) == pattern) {
            count++;
        }
    }
    cout << count;
    return 0;
}
