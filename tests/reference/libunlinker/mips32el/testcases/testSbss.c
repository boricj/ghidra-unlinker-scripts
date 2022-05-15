#include "test-helpers.h"

__attribute__((section(".sbss"))) int sbss_int;
__attribute__((section(".sbss"))) int sbss_int_array[4];

TESTCASE_READ(sbss_int, sbss_int)
TESTCASE_READ(sbss_int_array_0, sbss_int_array[0])
TESTCASE_READ(sbss_int_array_1, sbss_int_array[1])
TESTCASE_READ(sbss_int_array_2, sbss_int_array[2])
TESTCASE_READ(sbss_int_array_3, sbss_int_array[3])
TESTCASE_READ(sbss_int_array_a, sbss_int_array[a])
TESTCASE_READ(sbss_int_array_a_1, sbss_int_array[a+1])
TESTCASE_READ(sbss_int_array_a_b, sbss_int_array[a+b])
TESTCASE_READ(sbss_int_array_a_b_1, sbss_int_array[a+b+1])

TESTCASE_DATA(sbss_int, sbss_int)
TESTCASE_DATA(sbss_int_array_0, sbss_int_array[0])
TESTCASE_DATA(sbss_int_array_1, sbss_int_array[1])
TESTCASE_DATA(sbss_int_array_2, sbss_int_array[2])
TESTCASE_DATA(sbss_int_array_3, sbss_int_array[3])
TESTCASE_DATA(sbss_int_array_a, sbss_int_array[a])
TESTCASE_DATA(sbss_int_array_a_1, sbss_int_array[a+1])
TESTCASE_DATA(sbss_int_array_a_b, sbss_int_array[a+b])
TESTCASE_DATA(sbss_int_array_a_b_1, sbss_int_array[a+b+1])

TESTCASE_WRITE(sbss_int_val_0, sbss_int, 0)
TESTCASE_WRITE(sbss_int_array_0_val_0, sbss_int_array[0], 0)
TESTCASE_WRITE(sbss_int_array_1_val_0, sbss_int_array[1], 0)
TESTCASE_WRITE(sbss_int_array_2_val_0, sbss_int_array[2], 0)
TESTCASE_WRITE(sbss_int_array_3_val_0, sbss_int_array[3], 0)
TESTCASE_WRITE(sbss_int_array_a_val_0, sbss_int_array[a], 0)
TESTCASE_WRITE(sbss_int_array_a_1_val_0, sbss_int_array[a+1], 0)
TESTCASE_WRITE(sbss_int_array_a_b_val_0, sbss_int_array[a+b], 0)
TESTCASE_WRITE(sbss_int_array_a_b_1_val_0, sbss_int_array[a+b+1], 0)
