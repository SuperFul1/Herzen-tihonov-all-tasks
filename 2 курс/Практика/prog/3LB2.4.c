#include <stdio.h>
#include <stdlib.h>

struct MyUnion {
    union union_type {
        int number;
        char bytes[4];
    } the_union;

    enum {
        NUMBER,
        BYTES,
    } used_type;
};
int main (void) {
    struct MyUnion unions[5];
    int value;
    for (int i = 0; i < 5; i++){
        scanf("%i",&value);
        unions[i].the_union.number = value;
        unions[i].used_type = NUMBER;
    }
    for (int i = 0; i < 5; i++){
        printf("%i, ",unions[i].the_union.number);
        for (int j = 0; j < sizeof(int);j++){
            printf("%d ", unions[i].the_union.bytes[j] );
        }
        printf("\n");
    }
    return 0;
}