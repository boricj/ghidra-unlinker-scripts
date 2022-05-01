#pragma once

static const int __NR_Linux = 4000;
static const int __NR_syscall = (__NR_Linux + 0);
static const int __NR_exit = (__NR_Linux + 1);
static const int __NR_write = (__NR_Linux + 4);

#define __SYSCALL_CLOBBERS "$1", "$3", "$8", "$9", "$10", "$11", "$12", "$13", \
    "$14", "$15", "$24", "$25", "hi", "lo", "memory"

#define write(fd, buf, len) do {                            \
        register int v0 asm("v0") = __NR_write;             \
        register int a0 asm("a0") = fd;                     \
        register const void* a1 asm("a1") = buf;            \
        register int a2 asm("a2") = len;                    \
                                                            \
        asm volatile (                                      \
            "syscall"                                       \
            : "+r"(v0), "+r"(a0), "+r"(a1), "+r"(a2)        \
            :                                               \
            : "$7", __SYSCALL_CLOBBERS                      \
        );                                                  \
    } while (0)

#define exit(status) do {                                   \
        register int v0 asm("v0") = __NR_exit;              \
        register int a0 asm("a0") = status;                 \
                                                            \
        asm volatile (                                      \
            "syscall"                                       \
            : "+r"(v0), "+r"(a0)                            \
            :                                               \
            : "$5", "$6", "$7",__SYSCALL_CLOBBERS           \
        );                                                  \
                                                            \
        __builtin_unreachable();                            \
    } while (0)

#define putch(ch) do {                                      \
        const char _putch_data = ch;                        \
        write(1, &_putch_data, 1);                          \
    } while (0)
