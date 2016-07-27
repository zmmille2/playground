#include <stdlib.h>
#include <stdio.h>

int main(int argc, char** argv)
{
    void* ptr = malloc(10);
    char* ptr2 = (char*) ptr;
    int result = *(ptr2 + 1);
    free(ptr);
    return printf("%d\n", result);
}
