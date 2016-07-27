#include <stdio.h>
#include <stdlib.h>
#include <readline/readline.h>
#include <readline/history.h>

int main(int argc, char** argv)
{
    char* n = malloc(2 * sizeof(char));
    n[0] = 'c';
    n[1] = '\0';
    char* line = malloc(256);
    while(n != NULL)
    {
        n = fgets(line, 255, stdin);
        printf("%s", line);
    }
    free(line);
    free(n);
    return 1;
}
