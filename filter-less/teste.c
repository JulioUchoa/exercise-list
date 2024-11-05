#include "helpers.h"
#include <stdio.h>
#include <math.h>


// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {

            int ave = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);

            image[i][j].rgbtRed = ave;
            image[i][j].rgbtGreen = ave;
            image[i][j].rgbtBlue = ave;
        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {

            float sepred = image[i][j].rgbtRed * 0.393 + image[i][j].rgbtGreen * 0.769 + image[i][j].rgbtBlue * 0.189;
            float sepgreen = image[i][j].rgbtRed * 0.349 + image[i][j].rgbtGreen * 0.686 + image[i][j].rgbtBlue * 0.168;
            float sepblue = image[i][j].rgbtRed * 0.272 + image[i][j].rgbtGreen * 0.534 + image[i][j].rgbtBlue * 0.131;

            if (sepred > 255)
            {
                sepred = 255;
            }
            if (sepgreen > 255)
            {
                sepgreen = 255;
            }
            if (sepblue > 255)
            {
                sepblue = 255;
            }

            image[i][j].rgbtRed = (int) round(sepred);
            image[i][j].rgbtGreen = (int) round(sepgreen);
            image[i][j].rgbtBlue = (int) round(sepblue);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width/2 ; j++)
        {
           RGBTRIPLE temp = image[i][j];

           image[i][j] = image[i][width - j - 1];

           image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{


    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width-1; j++)
        {
// confere se estamos no limite superior da image
            if (copy[i - 1] == 0)
            {
// confere se estamos no limite superior esquerdo ==
                if (copy[j - 1] == 0)
                {
                    image[i][j].rgbtRed = round((copy[i][j].rgbtRed + copy[i][j+1].rgbtRed + copy[i + 1][j].rgbtRed + copy[i+1][j+1].rgbtRed)/4.0);
                    image[i][j].rgbtGreen = round((copy[i][j].rgbtGreen + copy[i][j+1].rgbtGreen + copy[i + 1][j].rgbtGreen + copy[i+1][j+1].rgbtGreen)/4.0);
                    image[i][j].rgbtBlue = round((copy[i][j].rgbtBlue + copy[i][j+1].rgbtBlue + copy[i + 1][j].rgbtBlue + copy[i+1][j+1].rgbtBlue)/4.0);
                }
// confere se estamos no limite superior direito ==>
                if (copy[j + 1] == 0)
                {
                    image[i][j].rgbtRed = round((copy[i][j].rgbtRed + copy[i][j-1].rgbtRed + copy[i+1][j-1].rgbtRed + copy[i + 1][j].rgbtRed)/4.0);
                    image[i][j].rgbtGreen = round((copy[i][j].rgbtGreen + copy[i][j-1].rgbtGreen + copy[i+1][j-1].rgbtGreen + copy[i + 1][j].rgbtGreen)/4.0);
                    image[i][j].rgbtBlue = round((copy[i][j].rgbtBlue + copy[i][j-1].rgbtBlue + copy[i+1][j-1].rgbtBlue + copy[i + 1][j].rgbtBlue)/4.0);
                }
// dá a média dos pixels que estão no limite superior com excessão dos ja citados a cima (limite superior direito/esquerdo)
                image[i][j].rgbtRed = round((copy[i][j].rgbtRed + copy[i][j-1].rgbtRed + copy[i][j+1].rgbtRed + copy[i+1][j-1].rgbtRed + copy[i + 1][j].rgbtRed + copy[i+1][j+1].rgbtRed)/6.0);
                image[i][j].rgbtGreen = round((copy[i][j].rgbtGreen + copy[i][j-1].rgbtGreen + copy[i][j+1].rgbtGreen + copy[i+1][j-1].rgbtGreen + copy[i + 1][j].rgbtGreen + copy[i+1][j+1].rgbtGreen)/6.0);
                image[i][j].rgbtBlue = round((copy[i][j].rgbtBlue + copy[i][j-1].rgbtBlue + copy[i][j+1].rgbtBlue + copy[i+1][j-1].rgbtBlue + copy[i + 1][j].rgbtBlue + copy[i+1][j+1].rgbtBlue)/6.0);
            }

// confere se estamos no limite inferior da image \/
            if (copy[i + 1] == 0)
            {
// confere se estamos no limite inferior esquerdo | < \/
                if (copy[j - 1] == 0)
                {
                    image[i][j].rgbtRed = round((copy[i][j].rgbtRed + copy[i][j+1].rgbtRed + copy[i-1][j+1].rgbtRed + copy[i - 1][j].rgbtRed)/4.0);
                    image[i][j].rgbtGreen = round((copy[i][j].rgbtGreen + copy[i][j+1].rgbtGreen + copy[i-1][j+1].rgbtGreen + copy[i - 1][j].rgbtGreen)/4.0);
                    image[i][j].rgbtBlue = round((copy[i][j].rgbtBlue + copy[i][j+1].rgbtBlue + copy[i-1][j+1].rgbtBlue + copy[i - 1][j].rgbtBlue)/4.0);
                }

// confere se estamos no limite inferior direito da imagem > \/
                if (copy[j + 1] == 0)
                {
                    image[i][j].rgbtRed = round((copy[i][j].rgbtRed + copy[i][j-1].rgbtRed + copy[i-1][j-1].rgbtRed + copy[i - 1][j].rgbtRed)/4.0);
                    image[i][j].rgbtGreen = round((copy[i][j].rgbtGreen + copy[i][j-1].rgbtGreen + copy[i-1][j-1].rgbtGreen + copy[i - 1][j].rgbtGreen)/4.0);
                    image[i][j].rgbtBlue = round((copy[i][j].rgbtBlue + copy[i][j-1].rgbtBlue + copy[i-1][j-1].rgbtBlue + copy[i - 1][j].rgbtBlue)/4.0);
                }

// confere se estamos no limite inferior da imagem com excessão dos já citados (limite inferior esquerdo, limite inferior direito)
                image[i][j].rgbtRed = round((copy[i][j].rgbtRed + copy[i][j - 1].rgbtRed + copy[i-1][j-1].rgbtRed + copy[i-1][j].rgbtRed + copy[i-1][j+1].rgbtRed + copy[i][j+1].rgbtRed)/6.0);
                image[i][j].rgbtGreen = round((copy[i][j].rgbtGreen + copy[i][j-1].rgbtGreen + copy[i-1][j-1].rgbtGreen + copy[i-1][j].rgbtGreen + copy[i-1][j+1].rgbtGreen + copy[i][j+1].rgbtGreen)/6.0);
                image[i][j].rgbtBlue = round((copy[i][j].rgbtBlue + copy[i][j-1].rgbtBlue + copy[i-1][j-1].rgbtBlue + copy[i-1][j].rgbtBlue + copy[i-1][j+1].rgbtBlue + copy[i][j+1].rgbtBlue)/6.0);
            }

// confere se estamos no limite esquerdo da imagem (com excessao do limite superior esquerdo e limite inferior esquerdo)
            if (copy[j-1] == 0)
            {
                image[i][j].rgbtRed = round((copy[i][j].rgbtRed + copy[i-1][j].rgbtRed + copy[i-1][j+1].rgbtRed + copy[i][j+1].rgbtRed + copy[i+1][j+1].rgbtRed + copy[i+1][j].rgbtRed)/6.0);
                image[i][j].rgbtGreen = round((copy[i][j].rgbtGreen + copy[i-1][j].rgbtGreen + copy[i-1][j+1].rgbtGreen + copy[i][j+1].rgbtGreen + copy[i+1][j+1].rgbtGreen + copy[i+1][j].rgbtGreen)/6.0);
                image[i][j].rgbtBlue = round((copy[i][j].rgbtBlue + copy[i-1][j].rgbtBlue + copy[i-1][j+1].rgbtBlue + copy[i][j+1].rgbtBlue + copy[i+1][j+1].rgbtBlue + copy[i+1][j].rgbtBlue)/6.0);
            }

// confere se estamos no limite direito da imagem ( com excessao do limite supeior dirieto e inferior direito)
            if (copy[j+1] == 0)
            {
                image[i][j].rgbtRed = round((copy[i][j].rgbtRed + copy[i-1][j].rgbtRed + copy[i-1][j-1].rgbtRed + copy[i][j-1].rgbtRed + copy[i+1][j-1].rgbtRed + copy[i+1][j].rgbtRed)/6.0);
                image[i][j].rgbtGreen = round((copy[i][j].rgbtGreen + copy[i-1][j].rgbtGreen + copy[i-1][j-1].rgbtGreen + copy[i][j-1].rgbtGreen + copy[i+1][j-1].rgbtGreen + copy[i+1][j].rgbtGreen)/6.0);
                image[i][j].rgbtBlue = round((copy[i][j].rgbtBlue + copy[i-1][j].rgbtBlue + copy[i-1][j-1].rgbtBlue + copy[i][j-1].rgbtBlue + copy[i+1][j-1].rgbtBlue + copy[i+1][j].rgbtBlue)/6.0);
            }

// dá a média dos pixels que têm 8 pixels em volta de si (estão no 'meio' da imagem)
            else
            {
                image[i][j].rgbtRed = round((copy[i][j].rgbtRed + copy[i-1][j-1].rgbtRed + copy[i-1][j].rgbtRed + copy[i-1][j+1].rgbtRed + copy[i][j-1].rgbtRed + copy[i][j+1].rgbtRed + copy[i+1][j-1].rgbtRed + copy[i + 1][j].rgbtRed + copy[i+1][j+1].rgbtRed)/9.0);
                image[i][j].rgbtGreen = round((copy[i][j].rgbtGreen + copy[i-1][j-1].rgbtGreen + copy[i-1][j].rgbtGreen + copy[i-1][j+1].rgbtGreen + copy[i][j-1].rgbtGreen + copy[i][j+1].rgbtGreen + copy[i+1][j-1].rgbtGreen + copy[i + 1][j].rgbtGreen + copy[i+1][j+1].rgbtGreen)/9.0);
                image[i][j].rgbtBlue = round((copy[i][j].rgbtBlue + copy[i-1][j-1].rgbtBlue + copy[i-1][j].rgbtBlue + copy[i-1][j+1].rgbtBlue + copy[i][j-1].rgbtBlue + copy[i][j+1].rgbtBlue + copy[i+1][j-1].rgbtBlue + copy[i + 1][j].rgbtBlue + copy[i+1][j+1].rgbtBlue)/9.0);
            }


        }
    }

    return;
}