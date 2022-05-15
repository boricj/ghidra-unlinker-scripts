#pragma once

#define TESTCASE_READ(name, variable) \
    int testcase_read_ ## name(int a, int b, int c, int d) { \
        return variable; \
    }
#define TESTCASE_WRITE(name, variable, value) \
    void testcase_write_ ## name(int a, int b, int c, int d) { \
        variable = value; \
    }
#define TESTCASE_DATA(name, variable) \
    int* testcase_data_ ## name(int a, int b, int c, int d) { \
        return &variable; \
    }
