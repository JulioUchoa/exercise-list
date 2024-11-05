#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    // Seccioned groups for better itereting
    char gp_1[20] = {'a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u', // 1 point
'A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'
                    };
    char gp_2[8] = {'b', 'c', 'm', 'p', 'B', 'C', 'M', 'P'};           // 3 points
    char gp_3[4] = {'d', 'g', 'D', 'G'};                               // 2 points
    char gp_4[10] = {'f', 'h', 'v', 'w', 'y', 'F', 'H', 'V', 'W', 'Y'};    // 4 points
    char gp_5[2] = {'k', 'K'};                                         // 5 points
    char gp_6[4] = {'j', 'x', 'J', 'X'};                               // 8 points
    char gp_7[4] = {'q', 'z', 'Q', 'Z'};                               // 10 points

// define cs variable to store sum of letter's values
    int cs = 0;
// for loop to iterate through every letter in word
    for (int i = 0; i < strlen(word); i++)
    {
// check if digit is alphabetical
        if(isalpha(word[i]))
        {
// iterate to check if first word is in frist sectioned group
            for (int j = 0; j < sizeof(gp_1); j++)
            {
                if (gp_1[j] == word[i])
                {
                    cs += 1;
                }
            }
// iterate to check if first word is in second sectioned group
            for (int n = 0; n < sizeof(gp_2); n++)
            {
                if (gp_2[n] == word[i])
                {
                    cs += 3;
                }
            }
// iterate to check if first word is in third sectioned group
            for (int m = 0; m < sizeof(gp_3); m++)
            {
                if (gp_3[m] == word[i])
                {
                    cs += 2;
                }
            }
// iterate to check if first word is in forth sectioned group
            for (int l = 0; l < sizeof(gp_4); l++)
            {
                if (gp_4[l] == word[i])
                {
                    cs += 4;
                }
            }
// iterate to check if first word is in fifth sectioned group
            for (int o = 0; o < sizeof(gp_5); o++)
            {
                if (gp_5[o] == word[i])
                {
                    cs += 5;
                }
            }
// iterate to check if first word is in sixth sectioned group
            for (int p = 0; p < sizeof(gp_6); p++)
            {
                if (gp_6[p] == word[i])
                {
                    cs += 8;
                }
            }
// iterate to check if first word is in seventh sectioned group
            for (int r = 0; r < sizeof(gp_7); r++)
            {
                if (gp_7[r] == word[i])
                {
                    cs += 10;
                }
            }
        }
        else
        {
            cs += 0;
        }
    }
    return cs;
}
