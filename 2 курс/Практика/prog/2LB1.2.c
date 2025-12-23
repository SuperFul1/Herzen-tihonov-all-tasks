#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *a = (int *) malloc(sizeof(int));
    int *b = (int *) malloc(sizeof(int));

    printf("vvedite dva chisla:\n");
    printf("____\n");
    scanf("%d\n", a);
    scanf("%d", b);
    printf("____\n");

    printf("Summa chisel: %d", *a + *b);

    free(a);
    free(b);

    return 0;
}