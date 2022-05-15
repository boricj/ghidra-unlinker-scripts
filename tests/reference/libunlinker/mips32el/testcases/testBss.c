#include "test-helpers.h"

__attribute__((section(".bss"))) int bss_int;
__attribute__((section(".bss"))) int bss_int_array[4];

TESTCASE_READ(bss_int, bss_int)
TESTCASE_READ(bss_int_array_0, bss_int_array[0])
TESTCASE_READ(bss_int_array_1, bss_int_array[1])
TESTCASE_READ(bss_int_array_2, bss_int_array[2])
TESTCASE_READ(bss_int_array_3, bss_int_array[3])
TESTCASE_READ(bss_int_array_a, bss_int_array[a])
TESTCASE_READ(bss_int_array_a_1, bss_int_array[a+1])
TESTCASE_READ(bss_int_array_a_b, bss_int_array[a+b])
TESTCASE_READ(bss_int_array_a_b_1, bss_int_array[a+b+1])

TESTCASE_DATA(bss_int, bss_int)
TESTCASE_DATA(bss_int_array_0, bss_int_array[0])
TESTCASE_DATA(bss_int_array_1, bss_int_array[1])
TESTCASE_DATA(bss_int_array_2, bss_int_array[2])
TESTCASE_DATA(bss_int_array_3, bss_int_array[3])
TESTCASE_DATA(bss_int_array_a, bss_int_array[a])
TESTCASE_DATA(bss_int_array_a_1, bss_int_array[a+1])
TESTCASE_DATA(bss_int_array_a_b, bss_int_array[a+b])
TESTCASE_DATA(bss_int_array_a_b_1, bss_int_array[a+b+1])

TESTCASE_WRITE(bss_int_val_0, bss_int, 0)
TESTCASE_WRITE(bss_int_array_0_val_0, bss_int_array[0], 0)
TESTCASE_WRITE(bss_int_array_1_val_0, bss_int_array[1], 0)
TESTCASE_WRITE(bss_int_array_2_val_0, bss_int_array[2], 0)
TESTCASE_WRITE(bss_int_array_3_val_0, bss_int_array[3], 0)
TESTCASE_WRITE(bss_int_array_3_val_a, bss_int_array[a], 0)
TESTCASE_WRITE(bss_int_array_a_1_val_0, bss_int_array[a+1], 0)
TESTCASE_WRITE(bss_int_array_a_b_val_0, bss_int_array[a+b], 0)
TESTCASE_WRITE(bss_int_array_a_b_1_val_0, bss_int_array[a+b+1], 0)
