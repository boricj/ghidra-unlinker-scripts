#include "test-helpers.h"

void testcase_flow_target() {
}

void testcase_flow_call() {
    asm volatile (
        "jal testcase_flow_target"
        :
        :
        :    
    );
}

void testcase_flow_call_indirect() {
    register void(*v0)(void) asm("v0") = testcase_flow_target;

    asm volatile (
        "jalr %0"
        :
        : "r"(v0)
        :    
    );
}

__attribute__((noreturn)) void testcase_flow_jump() {
    asm volatile (
        "j testcase_flow_target"
        :
        :
        :    
    );
    __builtin_unreachable();
}

void testcase_flow_jump_local(int i) {
    asm volatile (
        "beq %0, %0, .L998;"
        "addu $a0, $a0, $a0;"
        "j .L999;"
        ".L998:;"
        "addu $a2, $a2, $a2;"
        ".L999:;"
        "addu $a1, $a1, $a1;"
        :
        : "r"(i)
        :    
    );
}

__attribute__((noreturn)) void testcase_flow_jump_indirect() {
    register void(*v0)(void) asm("v0") = testcase_flow_target;

    asm volatile (
        "jr %0"
        :
        : "r"(v0)
        :    
    );
    __builtin_unreachable();
}
