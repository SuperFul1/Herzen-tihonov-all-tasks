#include <stdio.h>
#include <stdlib.h>

struct Birthday {
    unsigned int day : 5;
    unsigned int month : 4;
    unsigned int year : 15;
};

int main(int argc, char **argv) {
    struct Birthday date;
    date.day = 1;
    date.month = 12;
    date.year = 1997;

    printf("Birthday  is: %d.%d.%d", date.day, date.month, date.year);

    return 0;
}