#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int lista = '1, 2, 3, 4, 5'

    for (int i = 0; i < sizeof(lista); i++)
    {
        printf("%i \n", lista[i]);
    }

}