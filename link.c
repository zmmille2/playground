#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char** argv)
{
    char* path1 = "/etc/password";
    char* path2 = "some other thing";

    link(path1, path2);
    symlink(path1, path2);
    return 0;
}
