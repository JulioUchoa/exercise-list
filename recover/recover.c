#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


typedef uint8_t BYTE;   // define unsiged char type

const int BLOCK_SIZE = 512; // define const BLOCK_SIZE

int main(int argc, char *argv[])
{
    if (argc != 2) // check if user prompt right nº of arguments
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r"); // opens file

    if (card == NULL) // check if file opens properly
    {
        printf("file could not open! \n");
        return 2;
    }

    BYTE buffer[512]; // define array buffer of type BYTE with 512 elements

    int counter = 0; // define counter to check if its the first jpeg

    FILE *outp_file = NULL; // define File to store images

    char *filename = malloc(8 *sizeof(BYTE)); // define pointer to write in the jpeg name

    while(fread(buffer, sizeof(BYTE), 512, card) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            sprintf(filename, "%03i.jpg", counter);
            outp_file = fopen(filename, "w");
            counter++;
        }
        if  (outp_file != NULL)
        {
            fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, outp_file);
        }

    }
    fclose(card);
    fclose(outp_file);
    free(filename);
    return 0;
}