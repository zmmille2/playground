#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void handler(int signal);
int main(int argc, char** argv)
{
    signal(SIGALRM, handler);
    alarm(3);
    sleep(3);
    return 0;
}

void handler(int signal)
{
    printf("I got a signal!\n");
    return;
}
