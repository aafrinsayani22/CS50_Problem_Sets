#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Average surrounding pxl colors
            float colorSum = image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed;
            float Average = colorSum / 3;
            int roundedAverage = round(Average);
            // register new pxls
            image[i][j].rgbtRed = roundedAverage;
            image[i][j].rgbtGreen = roundedAverage;
            image[i][j].rgbtBlue = roundedAverage;
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
            // Sepia formula replacement
            float sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            float sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            float sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;

            int newRed = round(sepiaRed);
            int newGreen = round(sepiaGreen);
            int newBlue = round(sepiaBlue);


            image[i][j].rgbtRed = newRed ;
            image[i][j].rgbtGreen = newGreen;
            image[i][j].rgbtBlue = newBlue;

            // Verify the color ranges
            if (newRed > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else if (newRed < 0)
            {
                image[i][j].rgbtRed = 0;
            }
            if (newGreen > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else if (newGreen < 0)
            {
                image[i][j].rgbtGreen = 0;
            }
            if (newBlue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else if (newBlue < 0)
            {
                image[i][j].rgbtBlue = 0;
            }

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE orImage[height][width];
    float firstCopyRed;
    float firstCopyGreen;
    float firstCopyBlue;


    for (int i = 0; i < height; i++)
    {

        for (int j = 0; j < width ; j++)
        {
            orImage[i][j] = image[i][j];
        }

        for (int j = 0; j < width; j++)
        {
            // Copy current values of colors
            firstCopyRed = (orImage[i][j].rgbtRed);
            firstCopyGreen = (orImage[i][j].rgbtGreen);
            firstCopyBlue = (orImage[i][j].rgbtBlue);

            // Replace first pxl with last
            image[i][j].rgbtRed = orImage[i][(width - 1) - j].rgbtRed;
            image[i][j].rgbtGreen = orImage[i][(width - 1) - j].rgbtGreen;
            image[i][j].rgbtBlue = orImage[i][(width - 1) - j].rgbtBlue;

            // Replace last pxl with first
            orImage[i][(width - 1) - j].rgbtRed = firstCopyRed;
            orImage[i][(width - 1) - j].rgbtGreen = firstCopyGreen;
            orImage[i][(width - 1) - j].rgbtBlue = firstCopyBlue;


        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE ogImage[height][width];
    // Copy the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            ogImage[i][j] = image[i][j];
        }
    }

    // Checks the neighbouring pixels
    for (int i = 0, red, green, blue, counter; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            red = green = blue = counter = 0;

            // Prints current colors
            if (i >= 0 && j >= 0)
            {
                red += ogImage[i][j].rgbtRed;
                green += ogImage[i][j].rgbtGreen;
                blue += ogImage[i][j].rgbtBlue;
                counter++;
            }
            // Prints left side pixel
            if (i >= 0 && j - 1 >= 0)
            {
                red += ogImage[i][j - 1].rgbtRed;
                green += ogImage[i][j - 1].rgbtGreen;
                blue += ogImage[i][j - 1].rgbtBlue;
                counter++;
            }
            // Prints right side pixel
            if ((i >= 0 && j + 1 >= 0) && (i >= 0 && j + 1 < width))
            {
                red += ogImage[i][j + 1].rgbtRed;
                green += ogImage[i][j + 1].rgbtGreen;
                blue += ogImage[i][j + 1].rgbtBlue;
                counter++;
            }
            // Prints up-side pixel
            if (i - 1 >= 0 && j >= 0)
            {
                red += ogImage[i - 1][j].rgbtRed;
                green += ogImage[i - 1][j].rgbtGreen;
                blue += ogImage[i - 1][j].rgbtBlue;
                counter++;
            }
            // Prints down-side pixl
            if ((i + 1 >= 0 && j >= 0) && (i + 1 < height && j >= 0))
            {
                red += ogImage[i + 1][j].rgbtRed;
                green += ogImage[i + 1][j].rgbtGreen;
                blue += ogImage[i + 1][j].rgbtBlue;
                counter++;
            }
            // Prints left-upcorner pixel
            if (i - 1 >= 0 && j - 1 >= 0)
            {
                red += ogImage[i - 1][j - 1].rgbtRed;
                green += ogImage[i - 1][j - 1].rgbtGreen;
                blue += ogImage[i - 1][j - 1].rgbtBlue;
                counter++;
            }
            // Prints right-upcorner pixel
            if ((i - 1 >= 0 && j + 1 >= 0) && (i - 1 >= 0 && j + 1 < width))
            {
                red += ogImage[i - 1][j + 1].rgbtRed;
                green += ogImage[i - 1][j + 1].rgbtGreen;
                blue += ogImage[i - 1][j + 1].rgbtBlue;
                counter++;
            }
            // Prints left-downcorner pixel
            if ((i + 1 >= 0 && j - 1 >= 0) && (i + 1 < height && j - 1 >= 0))
            {
                red += ogImage[i + 1][j - 1].rgbtRed;
                green += ogImage[i + 1][j - 1].rgbtGreen;
                blue += ogImage[i + 1][j - 1].rgbtBlue;
                counter++;
            }
            // Prints right-downcorner pixel
            if ((i + 1 >= 0 && j + 1 >= 0) && (i + 1 < height && j + 1 < width))
            {
                red += ogImage[i + 1][j + 1].rgbtRed;
                green += ogImage[i + 1][j + 1].rgbtGreen;
                blue += ogImage[i + 1][j + 1].rgbtBlue;
                counter++;
            }

            // Averages the color of surrounding pixels
            image[i][j].rgbtRed = round(red / (counter * 1.0));
            image[i][j].rgbtGreen = round(green / (counter * 1.0));
            image[i][j].rgbtBlue = round(blue / (counter * 1.0));
        }
    }

    return;
}

