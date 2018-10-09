#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int patternCount(const string& pattern, const string& dna) {
    int count = 0;
    for (int i = 0; i < dna.size() - pattern.size(); i++) {
        if (dna.substr(i, pattern.size()) == pattern) {
            count++;
        }
    }

    return count;
}

int main() {

    int k;
    string dna;

    cin >> dna;
    cin >> k;

    vector<string> maxMers;
    vector<string> seen;
    int maxCount = -1;

    for (int i = 0; i < dna.size() - k; i++) {
        string kmer = dna.substr(i, k);
        if (find(seen.begin(), seen.end(), kmer) == seen.end()) {
            seen.push_back(kmer);
            int tmpCount = patternCount(kmer, dna);

            if (tmpCount > maxCount) {
                maxCount = tmpCount;
                maxMers.clear();
                maxMers.push_back(kmer);
            } else if (tmpCount == maxCount) {
                maxMers.push_back(kmer);
            }
        }
    }

    for (string kmer : maxMers) {
        cout << kmer << " ";
    }

    return 0;
}
