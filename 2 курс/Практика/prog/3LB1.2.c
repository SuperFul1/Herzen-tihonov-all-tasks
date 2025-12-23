#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct Vector {
    char name[10];
    double x1, x2, x3;
};

double dot_product(struct Vector a, struct Vector b){
    return a.x1 * b.x1 + a.x2 * b.x2 + a.x3 * b.x3;
}

struct Vector cross_product(struct Vector a, struct Vector b){
    struct Vector result;
    sprintf(result.name, "[%s, %s]", a.name,b.name);
    result.x1 = a.x2 * b.x3 - a.x3 * b.x2;
    result.x2 = a.x1 * b.x3 - a.x3 * b.x1;
    result.x3 = a.x1 * b.x2 - a.x2 * b.x1;
    return result;
};

double norm2(struct Vector a){
    return sqrt(a.x1 * a.x1 + a.x2 * a.x2 + a.x3 * a.x3);
}

void print_vector(struct Vector a){
    printf("%s = {%.2f, %.2f, %.2f}\n", a.name, a.x1, a.x2, a.x3);
}

int main(void){
    struct Vector a = {"a", 2.2, 3.1, 1.2};
    struct Vector b = {"b", 4.1, 2.4, 1.1};
    print_vector(a);
    print_vector(b);

    double dotp_ab = dot_product(a, b);
    printf("skalarnoe umnojenie: %.2f\n", dotp_ab);

    struct Vector cross_ab = cross_product(a, b);
    print_vector(cross_ab);

    printf("|%s| = %.2f\n", a.name, norm2(a));
    printf("|%s| = %.2f\n", b.name, norm2(b));
    printf("|%s| = %.2f\n", cross_ab.name, norm2(cross_ab));

    return 0;
}
