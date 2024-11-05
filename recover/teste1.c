#include <stdio.h>

int main(void)
{

    int *list = malloc(3 * sizeof(int));

    if (list == NULL)
    {
        return 1;
    }

    



    free(list);


}