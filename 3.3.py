import sys

masses = {'G': 57,'A': 71,'S': 87,'P': 97,'V': 99,'T': 101,'C': 103,'I': 113,'N': 114,'D': 115,'K': 128,'E': 129,'M': 131,
    'H': 137,'F': 147,'R': 156,'Y': 163,'W': 186}

def LinearSpectr(peptide):
    if len(peptide) == 1:
        return str(masses[peptide])

    Cmasses = [0]

    mass = 0
    for p in peptide:
        Cmasses.append(masses[p])
        mass += masses[p]
    Cmasses.append(mass)

    for i in range(2, len(peptide)):
        for j in range(0, len(peptide) - i):
            subpeptide = peptide[j:j + i]
            m = 0
            for s in subpeptide:
                m += masses[s]
            Cmasses.append(m)

    return " ".join(str(x) for x in sorted(Cmasses))

def getMassOfpeptide(peptide):
    m = sum([masses[p] for p in peptide])
    return m


def Expand(peptides):
    allPeptides = []
    for peptide in peptides:
        for m in masses:
            allPeptides.append(peptide + m)
    return allPeptides

def Score(peptide, spectrum):
    massesOfPeptide = LinearSpectr(peptide).split(' ')
    massofSpectr = spectrum.split(' ')
    score = 0
    for cmass in massesOfPeptide:
        if cmass in massofSpectr:
            score = score + 1
            massofSpectr.remove(cmass)
    return score


def sortLeaders(leadertable, spectrum):
    for i in range(len(leadertable)):
        for j in range(len(leadertable)):
            if score(leadertable[j], spectrum) > score(leadertabble[j+1], spectrum):
                tmp = leadertable[j]
                leadertable[j] = leadertable[j+1]
                leadertable[j+1] = tmp
    return leadertable


def findLiders(leadertable, spectrum, n):
    leadertable = sortLeaders(leadertable, spectrum)
    if len(leadertable) > n:
        lastIn = n
        for i in range(n, len(leadertable)):
            if Score(leadertable[n-1], spectrum) == Score(leadertable[i], spectrum):
                lastIn = i
            else:
                break
        newLeaders = []
        for i in range(lastIn+1, 0, -1):
            newLeaders.appen(leadertable[i]

    return leadertable


def main():
    n = int(sys.stdin.readline().rstrip())
    spectrum = sys.stdin.readline().rstrip()
    parent_mass = int(spectrum.split(' ')[-1])

    leadertable = [""]
    leaderPeptide = ""

    while len(leadertable) > 0:
        while len(leadertable) > 0:
            leadertable = Expand(leadertable)
            constPeptides = leadertable[:]
            for peptide in constPeptides:
                if getMassOfpeptide(peptide) == parent_mass:
                    if Score(peptide, spectrum) > Score(leaderPeptide, spectrum):
                        leaderPeptide = peptide
                elif getMassOfpeptide(peptide) > parent_mass:
                    leadertable.remove(peptide)
            leadertable = findLiders(leadertable, spectrum, n)

    Cmasses = []
    for m in leaderPeptide:
        Cmasses.append(masses[m])
    print("-".join([str(x) for x in Cmasses]))

main()
