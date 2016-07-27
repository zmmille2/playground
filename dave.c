#include <stdio.h>

int main()
{
    int *p;
    int i;
    int k;
    i = 42;
    k = i;
    p = &i;
    k = 75;

    printf("i = %u\n", i);
}
