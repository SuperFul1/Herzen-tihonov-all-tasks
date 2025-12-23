#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <stdbool.h>

union person{
    int age;
    int yearofbirth;
};

int main()
{
    union person *Me;
    Me = (void*)malloc(sizeof(union person));
    Me->age = 25;
    printf("%d\n", Me->age);

    Me->yearofbirth = 1997;
    printf("%d\n", Me->yearofbirth);
    free(Me);
    return 0;
}