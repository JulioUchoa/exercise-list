// First program on C
// including the libraries
#include <stdio.h>
#include <cs50.h>


int main(void)
{
    // asking name for printing it
    string name = get_string("Whats your name?");
    // printing grettings + name
    printf("Hello fellow %s\n", name);
}