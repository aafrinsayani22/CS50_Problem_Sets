#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)
{
    // Get user input
    string s = get_string("Text: ");

    // Count number of letters
    int letters = 0;
    for (int i = 0; i < strlen(s); i++)
    {
        if ((islower(s[i])) || (isupper(s[i])))
        {
            letters++;
        }
    }

    // Initial count of a word
    int words = 0;
    if (s[0] != 32)
    {
        words++;
    }

    // Count of  words
    for (int i = 0; i < strlen(s); i++)
    {
        if (isspace(s[i]))
        {
            if (s[i + 1] != 32)
            {
                words++;
            }
        }
    }

    // Count number of sentences
    int sentences = 0;
    for (int i = 0; i < strlen(s); i++)
    {
        if (s[i] == '.' || s[i] == '!' || s[i] == '?')
        {
            sentences++;
        }
    }

    // Calculations
    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;

    // Coleman - liau index
    float index = (0.0588 * L - 0.296 * S - 15.8);

    // Output
    if (round(index) >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (round(index) < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", (int)round(index));
    }
}
