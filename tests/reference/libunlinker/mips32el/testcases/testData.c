#include "test-helpers.h"

__attribute__((section(".data"))) int data_int = 1;
__attribute__((section(".data"))) int data_int_array[4] = { 2, 3, 4, 5 };

TESTCASE_READ(data_int, data_int)
TESTCASE_READ(data_int_array_0, data_int_array[0])
TESTCASE_READ(data_int_array_1, data_int_array[1])
TESTCASE_READ(data_int_array_2, data_int_array[2])
TESTCASE_READ(data_int_array_3, data_int_array[3])
TESTCASE_READ(data_int_array_a, data_int_array[a])
TESTCASE_READ(data_int_array_a_1, data_int_array[a+1])
TESTCASE_READ(data_int_array_a_b, data_int_array[a+b])
TESTCASE_READ(data_int_array_a_b_1, data_int_array[a+b+1])

TESTCASE_DATA(data_int, data_int)
TESTCASE_DATA(data_int_array_0, data_int_array[0])
TESTCASE_DATA(data_int_array_1, data_int_array[1])
TESTCASE_DATA(data_int_array_2, data_int_array[2])
TESTCASE_DATA(data_int_array_3, data_int_array[3])
TESTCASE_DATA(data_int_array_a, data_int_array[a])
TESTCASE_DATA(data_int_array_a_1, data_int_array[a+1])
TESTCASE_DATA(data_int_array_a_b, data_int_array[a+b])
TESTCASE_DATA(data_int_array_a_b_1, data_int_array[a+b+1])

TESTCASE_WRITE(data_int_val_0, data_int, 0)
TESTCASE_WRITE(data_int_array_0_val_0, data_int_array[0], 0)
TESTCASE_WRITE(data_int_array_1_val_0, data_int_array[1], 0)
TESTCASE_WRITE(data_int_array_2_val_0, data_int_array[2], 0)
TESTCASE_WRITE(data_int_array_3_val_0, data_int_array[3], 0)
TESTCASE_WRITE(data_int_array_a_val_0, data_int_array[a], 0)
TESTCASE_WRITE(data_int_array_a_1_val_0, data_int_array[a+1], 0)
TESTCASE_WRITE(data_int_array_a_b_val_0, data_int_array[a+b], 0)
TESTCASE_WRITE(data_int_array_a_b_1_val_0, data_int_array[a+b+1], 0)
