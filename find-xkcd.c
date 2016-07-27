#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>

void find(char* path, char* key);

int main(int argc, char** argv)
{
    find(getenv("HOME"), "xkcd-functional.png");
    return 0;
}

void find(char* path, char* key)
{
    struct stat s;
    struct dirent* dp;
    DIR* dirp = opendir(path);
    if(!dirp) { perror("Could not open directory"); return; }
    while ((dp = readdir(dirp)) != NULL)
    {
        char newpath[strlen(path) + strlen(dp->d_name) + 2];
        if(0 != strncmp(dp->d_name, ".", 1) && 0 != strncmp(dp->d_name, "..", 2))
        {
            sprintf(newpath, "%s/%s", path, dp->d_name);
            if(0 == strncmp(dp->d_name, key, strlen(key) + 1))
                printf("%s\n", dp->d_name);
        }
        if(0 == stat(newpath, &s) && S_ISDIR(s.st_mode))
            find(newpath, key);
    }
    closedir(dirp);
}
