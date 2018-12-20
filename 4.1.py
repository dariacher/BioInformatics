import itertools
import sys
def matches(pat1 , pat2):
    count = sum(a == b for a, b in zip(pat1, pat2))
    return count

def isKmer(dna, pattern, k, d):
    N = len(dna)
    for i in range(N-k+1):
        pat = dna[i:i+k]
        if k - matches(pat, pattern) <= d:
            return True
    return False

def produceDif(nucl):
    result = []
    for l1 in nucl:
        for l2 in nucl:
            for l3 in nucl:
                for l4 in nucl:
                    result.append(l1+l2+l3+l4)
    return result

def generateKmers(pattern, k, d):
    nucleotids = 'ACGT'
    patterns = []
    kmers = []
    patterns = produceDif(nucleotids)
    for i,j in enumerate(patterns):
        patterns[i] = ''.join(j)
    for j in patterns:
        if k - matches(pattern, j) <= d:
            kmers.append(j)
    return kmers

def MotifE(dna, k, d):
    patterns = []
    N = len(dna[0])
    S = set()
    for i in range(N-k+1):
        ptr = dna[0][i:i+k]
        p = generateKmers(ptr, k, d)
        for j in p:
            find = 0
            for string in dna:
                if isKmer(string, j,k, d):
                    find += 1
            if find == len(dna):
                S.add(j)
    s = ""
    for i in S:
        s += i + " "
    print(s)


def main():
    s = sys.stdin.read().split("\n")
    s[0] = s[0].split(" ")
    k = int(s[0][0])
    d = int(s[0][1])
    dna = []
    dna = s[1:]
    MotifE(dna, k, d)
main()
