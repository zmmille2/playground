#include <stdlib.h>
#include <stdio.h>

int main(int argc, char** argv) {
    void* self = malloc(sizeof(void*));
    self = &self;
    while(1) {
        printf("%p\n", self);
        self = *((void**) self);
    }
    return 0;
}
