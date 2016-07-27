#include <string.h>
#include <unistd.h>
#include <stdio.h>

char* checkdir(char* path, char* current);

int main(int argc, char** argv)
{
    if(argc != 2)
    {
        printf("Usage: ./checkdir \"path\"\n");
    }
    else
    {
        size_t size = 256;
        char buffer [256];
        getcwd(buffer, size);
        printf("%s\n", checkdir(argv[1], buffer));
    }
    return 0;
}

char* checkdir(char* path, char* current)
{
    if(0 == chdir(path))
    {
        chdir(current);
        return "true";
    }
    return "false";
}
