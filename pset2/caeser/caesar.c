#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// Get key with command - line argument
int main(int argc, string argv[])
{
    if (argc == 2)
    {

        for (int i = 0; i < strlen(argv[1]); i++)
        {
            for (int k = 0; k < strlen(argv[1]); k++)
            {
                if (isalpha(argv[1][k]))
                {
                    printf("Usage: ./ceasar key\n");
                    return 1;
                }
            }
            // Validating key[i]
            if (isdigit(argv[1][i]))
            {
                // Convert string to integer
                int key = atoi(argv[1]);

                // Get plaintext
                string s = get_string("plaintext: ");

                // Print ciphertext
                printf("ciphertext: ");
                for (int j = 0; j < strlen(s); j++)
                {
                    // Checks uppercase letter
                    if (isupper(s[j]))
                    {
                        s[j] = s[j] - 65;
                        char u = ((s[j] + key) % 26);
                        s[j] = u + 65;
                        u = u + 65;
                        printf("%c", toupper(u));
                    }

                    // Checks lowercase letter
                    else if (islower(s[j]))
                    {
                        s[j] = s[j] - 97;
                        char l = ((s[j] + key) % 26);
                        s[j] = l + 97;
                        l = l + 97;
                        printf("%c", tolower(l));
                    }
                    else
                    {
                        printf("%c", s[j]);
                    }
                }
                printf("\n");
                return 0;
            }

        }

    }
    else
    {
        printf("Usage: ./ceasar key\n");
        return 1;
    }
}
