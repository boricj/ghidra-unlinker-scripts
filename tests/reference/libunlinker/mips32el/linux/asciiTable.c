#include "linux-helpers.h"
#include "ctype.h"

void print_number(int num) {
    putch('0');

    for (int n = 2; n >= 0; n--) {
        int digit = (num >> (3 * n)) % 010;
        putch('0' + digit);
    }
}

typedef struct {
    int (*func)(int);
    char flag;
} ascii_property;

#define NUM_ASCII_PROPERTIES 11

const ascii_property s_ascii_properties[11] = {
    { isgraph, 'g', },
    { isprint, 'p', },
    { iscntrl, 'c', },
    { isspace, 's', },
    { ispunct, '!', },
    { isalnum, 'A', },
    { isalpha, 'a', },
    { isdigit, 'd', },
    { isxdigit, 'x', },
    { isupper, 'U', },
    { islower, 'l', },
};

__attribute__((noreturn)) void __start(void) {
    for (int i = 0; i < 128; i++) {
        print_number(i);
        putch(' ');

        if (isgraph(i))
            putch(i);
        else
            putch(' ');
        putch(' ');

        for (int j = 0; j < NUM_ASCII_PROPERTIES; j++) {
            const ascii_property *property = &s_ascii_properties[j];

            if (property->func(i))
                putch(property->flag);
            else
                putch(' ');
        }

        putch('\n');
    }

    exit(0);
}
