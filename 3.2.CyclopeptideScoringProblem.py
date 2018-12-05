import sys

masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def CycloSpectr(peptide):
    Cmasses = [0]
    massOfPeptide = 0
    cyclePeptide = peptide + peptide
    for i in peptide:
        Cmasses.append(masses[i])
        massOfPeptide += masses[i]
    Cmasses.append(massOfPeptide)
    for j in range(2, len(peptide)):
        for k in range(0, len(peptide)):
            subPeptide = cyclePeptide[k:k+j]
            mass = 0
            for i in subPeptide:
                mass+=masses[i]
            Cmasses.append(mass)
    return " ".join(str(x) for x in sorted(Cmasses))

def Score(peptide, spectr):
    massesOfPep = CycloSpectr(peptide).split(' ')
    massesOfSpec = spectr.split(' ')
    score = 0
    for eachmass in massesOfPep:
        if eachmass in massesOfSpec:
            score +=1
            massesOfSpec.remove(eachmass)
    return score

def main():
    peptide = sys.stdin.readline().rstrip()
    spectr = sys.stdin.readline().rstrip()
    print(Score(peptide, spectr))

if __name__ == '__main__':
    main()
