from cs50 import get_string

text = get_string("Text: ")

lenght = len(text)
letter = []
for i in range(1, int(lenght)):
    letter.append(text)

# For  count of letters
letters = 0
for i in range(len(text)):
    if (text[i].isalpha()):
        letters += 1

# For initializing the count of words
words = 0
if (str.isalpha(text[0])):
    words += 1

# For  count of words
for i in range(len(text)):
    if (str.isspace(text[i]) and not str.isspace(text[i+1])):
        words += 1

# Count the number of sentences
sentences = 0
for i in range(len(text)):
    if (text[i] == '.' or text[i] == '!' or text[i] == "?"):
        sentences += 1
# Calculations
L = (letters) / (words) * 100
S = (sentences) / (words) * 100

# Coleman - liau index
index = (0.0588 * L - 0.296 * S - 15.8)

# Output
if (round(index) >= 16):
    print("Grade 16+")
elif (round(index) < 1):
    print("Before Grade 1")
else:
    r = int(round(index))
    print(f"Grade {r}")