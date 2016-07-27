#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void handler(int signal);
int main(int argc, char** argv)
{
    signal(SIGINT, handler);
    sleep(100);
    return 0;
}

void handler(int signal)
{
    printf("\nOops! Did I take too long?\n");
    exit(0);
}
