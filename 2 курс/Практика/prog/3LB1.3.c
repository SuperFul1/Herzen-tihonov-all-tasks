#include <stdio.h>
#include <stdlib.h>

struct Complex {
    double r, im;
};

struct Complex com_pow(struct Complex a, int n ) {
    struct Complex result = {1,0};
    int q = 0;
    for (int i = 0; i<n;i++){
        q = result.r;
        result.r = result.r*a.r-result.im*a.im;
        result.im = q*a.im + result.im*a.r;
    }
    return result;
}

int main(void) {
    struct Complex z = {4,2};
    printf("z = %lf + %lf*i \n\n",z.r,z.im);
    int n = 8;
    struct Complex exz = {1,0};
    struct Complex p = {0.0};
    int f = 1;
    for( int i = 1; i < n; i++) {
        f = f*i;
        p = com_pow(z,i);
        exz.r = exz.r+p.r/f;
        exz.im = exz.im+p.im/f;
    }
    printf("exp(z) = %lf + %lf*i \n\n",exz.r,exz.im);
    return 0;
}