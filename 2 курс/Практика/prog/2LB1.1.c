#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    double **pointer = NULL;
    double *x = (double *) malloc(sizeof(double));;
    pointer = (void *) malloc(sizeof(void));
    *pointer = x;
    **pointer = 2;
    printf("%lf", **pointer);
    free(pointer);
    free(x);
    return 0;
}
