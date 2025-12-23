#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *a = (int *) malloc(sizeof(int));
    int *b = (int *) malloc(sizeof(int));

    scanf("%d%d", a, b);

    if (*a > *b) {
        printf("Maximalnoe chislo: %d", *a);
    }
    else {
        printf("Maximalnoe chislo: %d", *b);
    }

    free(a);
    free(b);

    return 0;
}