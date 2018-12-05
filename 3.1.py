import sys

masses = {'G': 57,'A': 71,'S': 87,'P': 97,'V': 99,'T': 101,'C': 103,'I': 113,'N': 114,'D': 115,'K': 128,'E': 129,'M': 131,
    'H': 137,'F': 147,'R': 156,'Y': 163,'W': 186}


def getMassOfPeptide(peptide):
    mass = 0
    for p in peptide:
        mass += masses[p]
    return mass

def CycloSpectr(peptide):
    Cmasses = [0]
    massOfPeptide = 0
    cyclePeptide = peptide + peptide
    for i in peptide:
        Cmasses.append(masses[i])
        massOfPeptide += masses[i]
    Cmasses.append(massOfPeptide)
    for j in range(2, len(peptide)):
        for k in range(len(peptide)):
            subPeptide = cyclePeptide[k:k+j]
            mass = 0
            for i in subPeptide:
                mass = mass + masses[i]
            Cmasses.append(mass)
    resultList = []
    sortedMasses = sorted(Cmasses)
    for p in sortedCmasses:
        resultList.append(str(p))
    result = " ".join(resultList)
    return result

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
        for j in range(len(peptide) - i):
            subpeptide = peptide[j:j + i]
            m = 0
            for s in subpeptide:
                m = m + masses[s]
            Cmasses.append(m)

    resultList = []
    sortedMasses = sorted(Cmasses)
    for p in sortedCmasses:
        resultList.append(str(p))
    result = " ".join(resultList)
    return result

def Expand(peptides):
    allPeptides = []
    for peptide in peptides:
        for m in masses:
            allPeptides.append(peptide + m)
    return allPeptides


def Consistent(peptide, spectrum):
    massOfPeptide = []
    linSpectr = LinearSpectr(peptide).split(" ")
    for ls in linSpectr:
        massOfPeptide.append(int(ls))
    massOfSpectr = []
    spectr = spectrum.split(" ")
    for ls in spectr:
        massOfSpectr.append(int(ls))
    
    for mass in massofPeptide:
        if mass not in massOfSpectr:
            return False
    return True


def checkup(spectrum, parentMass):
    finishPeptides = []
    peptides=[""]
    while len(peptides) > 0:
        peptides = Expand(peptides)
        constPeptides = peptides[:]
        for peptide in constPeptides:
            if getMassOfPeptide(peptide) == parentMass:
                if CycloSpectr(peptide).strip() == spectrum.strip():
                    finishPeptides.append(peptide)
                peptides.remove(peptide)
            elif not Consistent(peptide, spectrum):
                peptides.remove(peptide)
    return finishPeptides

def main():
    spectrum = sys.stdin.readline().rstrip()
    parentMass = int(spectrum.split(' ')[-1])

    checkup(spectrum, parentMass)

    Cmasses = []
    for i in finishPeptides:
        mass = []
        for j in i:
            mass.append(masses[j])
        Cmasses.append('-'.join([str(x) for x in mass]))
    print(" ".join(Cmasses))

main()
