#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char** argv)
{
    int fd[2];
    int read_end = fd[0];
    int write_end = fd[1];
    if(0 == fork())
    {
        sleep(1);
        close(read_end);
        dup2(STDOUT_FILENO, write_end);
        printf("using dup haha can't wait for you to read this!\n");
        exit(0);
    }
    close(write_end);
    dup2(read_end, STDOUT_FILENO);
    wait(NULL);
    sleep(1);
    return 0;
}
