/**
 * @file stacktests.c
 * @author Kieran Ahn
 * @brief Tests for stack.c
 * @version 0.1
 * @date 2023-06-09
 * 
 * @copyright Copyright (c) 2023
 * 
 */

#include <assert.h>
#include <stdio.h>
#include <limits.h>
#include "stack.h"

int main() {

    // To test validation, uncomment these lines.
    
    // printf("Testing: initializing stack with negative capacity\n");
    // StringStack* negativeCapacityStack = stack_create(-1);
    
    // printf("Testing: initializing stack with 0 capacity\n");
    // StringStack* zeroCapacityStack = stack_create(0);

    // printf("Testing: preventing pop from stack while stack is empty\n");
    // StringStack* zeroSizePopStack = stack_create(10);
    // stack_pop(zeroSizePopStack);

    // printf("Testing: stack overflow prevention\n");
    // StringStack* stackFullStack = stack_create(1);
    // stackFullStack->top = 1;
    // stack_push(stackFullStack, "I'm a stack overflow!");

    // printf("Testing: stack capacity cannot overflow");
    // StringStack* stackCapacityOverflowStack = stack_create(INT_MAX);
    // stackCapacityOverflowStack->top = INT_MAX - 1;
    // stack_push(stackCapacityOverflowStack, "Capacity become large!");

    StringStack* stack = stack_create(10);
    assert(stack->capacity == 10);
    assert(stack_is_empty(stack));
    
    char* hello = "Hello";
    char* world = "World!";
    char* three = "three";
    char* four = "four";
    char* five = "five";
    char* six = "six";
    char* seven = "seven";
    char* eight = "eight";
    char* nine = "nine";
    char* ten = "ten";
    char* eleven = "eleven";
    stack_push(stack, hello);
    stack_push(stack, world);

    assert(stack->top == 1);
    stack_push(stack, three);
    stack_push(stack, four);
    stack_push(stack, five);
    stack_push(stack, six);
    stack_push(stack, seven);
    stack_push(stack, eight);
    stack_push(stack, nine);
    stack_push(stack, ten);
    stack_push(stack, eleven);

    assert(stack->top == 10);
    assert(stack->capacity = 20);

    char* lastHead;
    lastHead = stack_pop(stack);
    lastHead = stack_pop(stack);
    lastHead = stack_pop(stack);
    lastHead = stack_pop(stack);
    lastHead = stack_pop(stack);
    lastHead = stack_pop(stack);
    lastHead = stack_pop(stack);
    lastHead = stack_pop(stack);
    lastHead = stack_pop(stack);

    assert(stack->top == 1);
    assert(stack_peek(stack) == world);
    assert(stack_pop(stack) == world);
    assert(stack->capacity == 5);





    return 0;
}