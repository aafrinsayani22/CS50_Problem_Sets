#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // Ensure one command-line argument
    if (argc != 2)
    {
        return 1;
    }
    // Open memory card
    FILE *memory_card = fopen(argv[1], "r");
    if (memory_card == NULL)
    {
        return 2;
    }

    uint8_t buffer[512];
    int jpeg_found = 0;
    char filenames[8];
    FILE *image = NULL;
    // Repeat until end of card
    while (fread(buffer, 512, 1, memory_card))
    {
        // Start of JPEG?
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If already open first jpeg then close it
            if (image != NULL)
            {
                fclose(image);
            }

            // Create new jpeg file
            sprintf(filenames, "%03i.jpg", jpeg_found);
            image = fopen(filenames, "w");
            jpeg_found++;


        }
        // If already opened the jpeg then start writing
        if (image != NULL)
        {
            fwrite(buffer, 512, 1, image);
        }

    }
    // Close the image file if got all the images
    if (image != NULL)
    {
        fclose(image);
    }
    // Close memory card file
    fclose(memory_card);
    return 0;


}