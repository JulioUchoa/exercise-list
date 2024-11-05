// Including libraries we will need.
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

// declare functions
int count_letters(string text);
int count_words(string);
int count_sentences(string texto);

int main(void)
{
// prompt user for text input
    string texto = get_string("Digit a text:");

// addressing couting letters function to int variable
    float letters = count_letters(texto);

// adressing counting words fucntions to int variable
    float words = count_words(texto);

// addressing counting sentences function to int variable
    float sentences = count_sentences(texto);

// get avarage n of letters per 100 words
    float L = letters / words * 100;

// get avarage number of sentences per 100 words
    float S = sentences / words * 100;

// calculate Coleman-Liau Index
    float index = 0.0588 * L - 0.296 * S - 15.8;

// set condition to print the grade in accord with index values
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(index));
    }
}
// function for counting sentences
int count_sentences(string texto)
{
//counter
    int h = 0;
// for loop to iterate through the text and count
// how many "." there is
    for (int i = 0; i < strlen(texto); i++)
    {
        if (texto[i] == '.' || texto[i] == '!' || texto[i] == '?')
        {
            h ++;
        }
    }
    return h;
}
// function for counting words
int count_words(string texto)
{
// counter
    int m = 1;
// for loop iterate through text and count how many spaces
// so we can determine the number of words
    for (int i = 0; i < strlen(texto); i++)
    {
        if (isspace(texto[i]))
        {
            m++;
        }
    }
    return m;
}
// function for counting letters
int count_letters(string texto)
{
// counter
    int n = 0;
// loop for analizing every character of the text
    for (int i = 0; i < strlen(texto); i++)
    {
// condition to take apart what is letter and what isn't
        if (isalpha(texto[i]))
        {
            n++;
        }
    }
    return n;
}