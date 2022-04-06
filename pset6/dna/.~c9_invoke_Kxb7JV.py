# Iclude libraries
import sys
import csv

# Check for the correct input
if (len(sys.argv) != 3):
    print("Incorrect usage.")
    sys.exit(1)
# Open csv file
elif(len(sys.argv) == 3):
    with open(sys.argv[1], "r") as file1:
        reader1 = csv.DictReader(file1)
# Open text(sequence) file

    with open(sys.argv[2],"r") as file2:
        reader2 = csv.DictReader(file2)

        dnaSequence = file2.read()

        file2Lenght = len(dnaSequence)

    STR1 = STR2 = STR3 = STR4 = STR5 = STR6 = STR7 = STR8 = 0

    # For STR1
    for i in range(file2Lenght):
        # Check for STR 'AGATC'
        if (dnaSequence[i] == 'A'):
            if dnaSequence[i:(i + 5)] == ('AGATC'):
                STR1 += 1

    # For STR2
    for i in range(file2Lenght):
        # Check for STR 'TTTTTTCT'
        if (dnaSequence[i] == 'T'):
            if dnaSequence[i:(i + 8)] == ('TTTTTTCT'):
                STR2 += 1

    # For STR3
    for i in range(file2Lenght):
        # Check for STR 'AATG'
        if (dnaSequence[i] == 'A'):
            if dnaSequence[i:(i + 4)] == ('AATG'):
                STR3 += 1

    # For STR4
    for i in range(file2Lenght):
        # Check for STR 'TCTAG'
        if (dnaSequence[i] == 'T'):
            if dnaSequence[i:(i + 5)] == ('TCTAG'):
                STR4 += 1

    # For STR5
    for i in range(file2Lenght):
        # Check for STR 'GATA'
        if (dnaSequence[i] == 'G'):
            if dnaSequence[i:(i + 4)] == ('GATA'):
                STR5 += 1


    # For STR6
    for i in range(file2Lenght):
        # Check for STR 'TATC'
        if (dnaSequence[i] == 'T'):
            if dnaSequence[i:(i + 4)] == ('TATC'):
                STR6 += 1

    # For STR7
    for i in range(file2Lenght):
        # Check for STR 'GAAA'
        if (dnaSequence[i] == 'G'):
            if dnaSequence[i:(i + 4)] == ('GAAA'):
                STR7 += 1

    # For STR8
    for i in range(file2Lenght):
        # Check for STR 'TCTG'
        if (dnaSequence[i] == 'G'):
            if dnaSequence[i:(i + 4)] == ('TCTG'):
                STR8 += 1

    # Store the STR counts in a list
    STR_counts = []
    STR_counts.append(STR1)
    STR_counts.append(STR2)
    STR_counts.append(STR3)
    STR_counts.append(STR4)
    STR_counts.append(STR5)
    STR_counts.append(STR6)
    STR_counts.append(STR7)
    STR_counts.append(STR8)