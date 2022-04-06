// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 65536;

// Hash table
node *table[N];
char var_word[LENGTH + 1];
int total_words = 0;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Open the dictionary file to read
    FILE *NEW_DICTIONARY = fopen(dictionary, "r");
    if (NEW_DICTIONARY == NULL)
    {
        return 1;
    }
    // Read strings file
    while (fscanf(NEW_DICTIONARY, "%s", var_word) != EOF)
    {
        // Create a new Node
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            unload();
            return 2;
        }
        // Copy string from the word variable to the new_node word array
        strcpy(new_node -> word, var_word);

        // Find the index of the word through hash
        int index = hash(new_node -> word);
        node *head = new_node;

        // If the index is empty then fill the new node
        if (table[index] == NULL)
        {
            head  = new_node;
            new_node -> next = NULL;
            table[index] = head;
        }
        // Else if not occupied then link through it
        else
        {
            new_node -> next  = head;
            head = new_node;
        }
        total_words++;
    }
    fclose(NEW_DICTIONARY);
    return true;
}
// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int len = strlen(word);
    char buffer[len + 1];
    for (int i = 0; i < len; i++)
    {
        buffer[i] = tolower(word[i]);
    }
    buffer[len] = '\0';

    // create index from the word
    int index = hash(buffer);

    // look at the hashtable at position of index
    if (table[index] == NULL)
    {
        return false;
    }

    // create cursor
    node *head = table[index];
    node *cursor = head;

    // while hashtable is not empty, compare words
    while (cursor != NULL)
    {
        if (strcasecmp(cursor -> word, word) != 0)
        {
            cursor = cursor->next;
        }
        else
        {
            return true;
        }

    }

    // if no word; return false
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int hash = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        hash = (hash << 2) ^ word[i];
    }
    return hash % N;
}
// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return total_words;
    return 0;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *head = table[i];
        node *cursor = head;

        while (cursor != NULL)
        {

            node *tmp = cursor;
            cursor = cursor -> next;
            free(tmp);
        }
    }
    return true;
}
