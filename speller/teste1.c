#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>

// declare functions
int hasht(char);

int main (void)
{
    string a = get_string("digit a letter: \n");
    if (!isdigit(a))
    {
        printf("You must chose a letter. \n");
    }
    hasht(a);
    return 0;
}

int hasht(char a)
{
    x = a - 15;
    return x;
}