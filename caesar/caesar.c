#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>

//declare function prototype
bool only_digits(char s);
char rotate(char c, int n);

int main(int argc, string argv[])
{

//  1º check if command argument has only one input
    if (argc == 1 || argc != 2)
    {
        printf("Usage: /caesar key \n");
        return 1;
    }

// 2º make sure user's input is digit
    string teste = argv[1];
    for (int i = 0; i < strlen(teste); i++)
    {
        if (only_digits(teste[i]) == false)
        {
            printf("Usage: .caesar key\n");
            return 1;
        }

    }

// 3º convert argv[1] from string to an int
    int k = atoi(argv[1]);

// 4º prompt user for input plaintext
    string plaintext = get_string("plaintext: \n");

// 5º for loops to iterate through every char and change it in accord with key chosen
    printf("ciphertext:");
    for (int i = 0; i < strlen(plaintext); i++)
    {
        rotate(plaintext[i], k);
    }
    printf("\n");
    return 0;

}
// function checks if K input are digits
bool only_digits(char s)
{
    if (isdigit(s))
    {
        return 1;
    }
    else
    {
        return 0;
    }
    return 0;
}

// function to rotate every char as needed
char rotate(char c, int k)
{
    int j = c + k;
    if (isalpha(c))
    {
        if (isupper(c))
        {
            while (j > 90)
            {
                j = j - 26;
            }
        }
        else
        {
            while (j > 122)
            {
                j = j - 26;
            }
        }
        printf("%c", j);
    }
    else
    {
        printf("%c", c);
    }
    return 0;
}