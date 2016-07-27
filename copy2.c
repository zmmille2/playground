#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char** argv)
{
    if(argc != 3)
    {
        printf("Usage: ./copy \"source\" \"destination\"\n");
    }
    else
    {
        FILE* file_to_read = fopen(argv[1], "r");
        FILE* file_to_write = fopen(argv[2], "w");
        char* line = malloc(4096 * sizeof(char));
        int fd_to_read;
        int fd_to_write;
        size_t buffer = 0;
        size_t size;

        if(file_to_read != NULL)
        {
            fd_to_read = fileno(file_to_read);
            fd_to_write = fileno(file_to_write);
            while(0 != (size = read(fd_to_read, line, 4096)))
            {
                write(fd_to_write, line, size);
            }
        }
        free(line);
        fclose(file_to_read);
        fclose(file_to_write);
    }
    return 0;
}
