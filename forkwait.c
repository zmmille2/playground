#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int main(int argc, char** argv)
{
    pid_t child_pid = fork();
    int status;
    if(0 == child_pid)
    {
        sleep(1);
        printf("I'm the child!\n");
    }
    else
    {
        printf("This should print before the child.\n");
        waitpid(child_pid, &status, 0);
        printf("This should print after the child.\n");
    }
    return 0;
}
