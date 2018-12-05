import sys
masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

def getMassOfPeptide(peptide):
    mass = 0
    for i in peptide:
        mass += masses[i]
    return mass


def linearSpectr(peptide):
    if len(peptide) == 1:
        return str(masses[peptide])
    Cmasses = [0]
    massOfPeptide = 0
    for i in peptide:
        Cmasses.append(masses[i])
        massOfPeptide += masses[i]
    Cmasses.append(massOfPeptide)
    for j in range(2, len(peptide)):
        for k in range(0, len(peptide)):
            subPeptide = peptide[k:k+j]
            mass = 0
            for i in subPeptide:
                mass+=masses[i]
            Cmasses.append(mass)
    return " ".join(str(x) for x in sorted(Cmasses))


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

def Expand(peptides):
    allPeptides = []
    for eachPeptide in peptides:
        for m in masses:
            allPeptides.append(eachPeptide + m)
    return allPeptides

def Consistent(peptide, spectrum):
    massOfPeptide = [int(x) for x in linearSpectr(peptide).split(' ')]
    massOfSpectrum = [int(x) for x in spectrum.split(' ')]
    for eachMass in massOfPeptide:
        if eachMass in massOfSpectrum:
            pass
        else:
            return False
    return True

def main():
    spectrum = sys.stdin.readline().rstrip()
    parentMass = int(spectrum.split(' ')[-1])

    peptides = [""]
    finishPeptides = []

    while len(peptides) > 0:
        peptides = Expand(peptides)
        peptides1 = peptides[:]
        for peptide in peptides1:
            if getMassOfPeptide(peptide) == parentMass:
                if CycloSpectr(peptide).strip() == spectrum.strip():
                    finishPeptides.append(peptide)
                peptides.remove(peptide)
            elif not Consistent(peptide, spectrum):
                peptides.remove(peptide)
    Cmasses = []
    for pep in finishPeptides:
        mass = []
        for i in pep:
            mass.append(masses[i])
        Cmasses.append('-'.join([str(x) for x in mass]))
    print(" ".join(Cmasses))

    if __name__ == '__main__':
        main()
