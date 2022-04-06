# Iclude libraries
import sys
import csv

# Check for the correct input
if (len(sys.argv) != 3):
    print("Incorrect usage.")
    sys.exit(1)
# Open csv files
elif sys.argv[1] == ("databases/small.csv"):

    # Open file for small database
    smallfile = open(sys.argv[1], "r")
    readSmall = csv.DictReader(smallfile, delimiter=',')
    # Open sequences
    sequences = open(sys.argv[2], "r")
    readsequences = csv.DictReader(sequences, delimiter=',')
    # Read sequences
    dnaSequence = sequences.read()
    # Calculate lenght of sequence
    sequenceLength = len(dnaSequence)

    count = 0
    countAGATC = countAATG = countTATC = 0

    # Count for AGATC
    for i in range(sequenceLength):
        if (dnaSequence[i] == 'A'):
            if dnaSequence[i:(i + 5)] == ('AGATC'):
                count = 1
                for j in range((i + 5), sequenceLength, 5):
                    if dnaSequence[j: (j + 5)] == ('AGATC'):
                        count += 1
                    else:
                        break
                if (count > countAGATC):
                    countAGATC = count
                count = 0

    # Count for  'AATG'
    for i in range(sequenceLength):
        if (dnaSequence[i] == 'A'):
            if dnaSequence[i:(i + 4)] == ('AATG'):
                count = 1
                for j in range((i + 4), sequenceLength, 4):
                    if dnaSequence[j: (j + 4)] == ('AATG'):
                        count += 1
                    else:
                        break
                if (count > countAATG):
                    countAATG = count
                count = 0
    # Count for 'TATC'
    for i in range(sequenceLength):
        if (dnaSequence[i] == 'T'):
            if dnaSequence[i:(i + 4)] == ('TATC'):
                count = 1
                for j in range((i + 4), sequenceLength, 4):
                    if dnaSequence[j: (j + 4)] == ('TATC'):
                        count += 1
                    else:
                        break
                if (count > countTATC):
                    countTATC = count
                count = 0

    # Make a list of counts
    STR_counts = []
    STR_counts.append(countAGATC)
    STR_counts.append(countAATG)
    STR_counts.append(countTATC)

    # Print name if all counts matches with any person in csv file
    for row in readSmall:
        if ((STR_counts[0] == int(row["AGATC"]))
            and (STR_counts[1] == int(row["AATG"]))
                and (STR_counts[2] == int(row["TATC"]))):
            print(row["name"])
            sys.exit(0)

    print("No match.")


else:
    # Open csv for large databases
    largefile = open(sys.argv[1], "r")
    readLarge = csv.DictReader(largefile, delimiter=',')
    # Open text(sequence) file
    sequences = open(sys.argv[2], "r")
    readsequences = csv.DictReader(sequences, delimiter=',')
    # Read sequences
    dnaSequence = sequences.read()
    # Count length of the sequence
    sequenceLength = len(dnaSequence)

    countAGATC = countTTTTTTCT = countAATG = countTCTAG = countGATA = countTATC = countGAAA = countTCTG = 0

    # Count for 'AGATC'
    for i in range(sequenceLength):
        if (dnaSequence[i] == 'A'):
            if dnaSequence[i:(i + 5)] == ('AGATC'):
                count = 1
                for j in range((i + 5), sequenceLength, 5):
                    if dnaSequence[j: (j + 5)] == ('AGATC'):
                        count += 1
                    else:
                        break
                if (count > countAGATC):
                    countAGATC = count
                count = 0

    # Count for 'TTTTTTCT'
    for i in range(sequenceLength):
        if (dnaSequence[i] == 'T'):
            if dnaSequence[i:(i + 8)] == ('TTTTTTCT'):
                count = 1
                for j in range((i + 8), sequenceLength, 8):
                    if dnaSequence[j: (j + 8)] == ('TTTTTTCT'):
                        count += 1
                    else:
                        break
                if (count > countTTTTTTCT):
                    countTTTTTTCT = count
                count = 0

    # Count for 'AATG'
    for i in range(sequenceLength):
        if (dnaSequence[i] == 'A'):
            if dnaSequence[i:(i + 4)] == ('AATG'):
                count = 1
                for j in range((i + 4), sequenceLength, 4):
                    if dnaSequence[j: (j + 4)] == ('AATG'):
                        count += 1
                    else:
                        break
                if (count > countAATG):
                    countAATG = count
                count = 0

    # Count for 'TCTAG'
    for i in range(sequenceLength):
        if (dnaSequence[i] == 'T'):
            if dnaSequence[i:(i + 5)] == ('TCTAG'):
                count = 1
                for j in range((i + 5), sequenceLength, 5):
                    if dnaSequence[j: (j + 5)] == ('TCTAG'):
                        count += 1
                    else:
                        break
                if (count > countTCTAG):
                    countTCTAG = count
                count = 0

    # Count for 'GATA'
    for i in range(sequenceLength):
        if (dnaSequence[i] == 'G'):
            if dnaSequence[i:(i + 4)] == ('GATA'):
                count = 1
                for j in range((i + 4), sequenceLength, 4):
                    if dnaSequence[j: (j + 4)] == ('GATA'):
                        count += 1
                    else:
                        break
                if (count > countGATA):
                    countGATA = count
                count = 0

    # Count for 'TATC'
    for i in range(sequenceLength):
        if (dnaSequence[i] == 'T'):
            if dnaSequence[i:(i + 4)] == ('TATC'):
                count = 1
                for j in range((i + 4), sequenceLength, 4):
                    if dnaSequence[j: (j + 4)] == ('TATC'):
                        count += 1
                    else:
                        break
                if (count > countTATC):
                    countTATC = count
                count = 0

    # Count for 'GAAA'
    for i in range(sequenceLength):
        if (dnaSequence[i] == 'G'):
            if dnaSequence[i:(i + 4)] == ('GAAA'):
                count = 1
                for j in range((i + 4), sequenceLength, 4):
                    if dnaSequence[j: (j + 4)] == ('GAAA'):
                        count += 1
                    else:
                        break
                if (count > countGAAA):
                    countGAAA = count
                count = 0

    # Count for  'TCTG'
    for i in range(sequenceLength):
        if (dnaSequence[i] == 'T'):
            if dnaSequence[i:(i + 4)] == ('TCTG'):
                count = 1
                for j in range((i + 4), sequenceLength, 4):
                    if dnaSequence[j: (j + 4)] == ('TCTG'):
                        count += 1
                    else:
                        break
                if (count > countTCTG):
                    countTCTG = count
                count = 0

    # Store the STR counts in a list
    STR_counts = []
    STR_counts.append(countAGATC)
    STR_counts.append(countTTTTTTCT)
    STR_counts.append(countAATG)
    STR_counts.append(countTCTAG)
    STR_counts.append(countGATA)
    STR_counts.append(countTATC)
    STR_counts.append(countGAAA)
    STR_counts.append(countTCTG)

    # Print name if STR_counts matches with any person in csv file
    for row in readLarge:
        if ((STR_counts[0] == int(row["AGATC"]))
            and (STR_counts[1] == int(row["TTTTTTCT"]))
            and (STR_counts[2] == int(row["AATG"]))
            and (STR_counts[3] == int(row["TCTAG"]))
            and (STR_counts[4] == int(row["GATA"]))
            and (STR_counts[5] == int(row["TATC"]))
            and (STR_counts[6] == int(row["GAAA"]))
                and (STR_counts[7] == int(row["TCTG"]))):
            print(row["name"])
            sys.exit(0)

    print("No match.")
# Close all opened files
smallfile.close()
largefile.close()
sequences.close()
sequences.close()