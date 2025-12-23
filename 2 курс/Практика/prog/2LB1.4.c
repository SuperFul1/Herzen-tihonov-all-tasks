#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    printf(" vhodnaya dlina massiva:\n");
    scanf("%d", &n);
    double *A = (double *) malloc (n * sizeof(double));
    double *p;
    printf(" vvedite chislo:\n");
    for (p = A; p - A < n; p++) {
        scanf("%lf", p);
    }
    printf("\n vash massiv:\n");

    for (p = A; p - A < n; p++) {
        printf("%lf\n", *p);
    }

    free(A);

    return 0;
}