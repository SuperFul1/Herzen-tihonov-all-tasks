#include <stdio.h>
#include <stdlib.h>

union prog {
    unsigned long a;
    char b[8];
};

int main(void) {
    union prog del;
    del.a = 12391;
    int i;
    for (i = 0; i <=7; i++) {
        printf("%d ", del.b[i]);
    }
    return 0;
}