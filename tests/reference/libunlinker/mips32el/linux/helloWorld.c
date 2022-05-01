#include "linux-helpers.h"

const char S_HELLO_WORLD[] = "Hello, world!\n";

__attribute__((noreturn)) void __start(void) {
    write(1, S_HELLO_WORLD, sizeof(S_HELLO_WORLD) - 1);
    exit(0);
}
