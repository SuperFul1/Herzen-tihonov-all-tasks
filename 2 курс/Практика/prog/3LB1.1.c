#include <stdio.h>
#include <stdlib.h>

struct Operation {
    char op;
    int (*func) (int, int);
};

int add (int a, int b) {
    return a + b;
}

int main()
{
    struct Operation op1 = {'+', &add};

    int a = 4, b = 6;
    printf("%d %c %d = %d", a, op1.op, b, op1.func(a, b));
    return 0;
}