#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stack.h"

#define STACK_UNDERFLOW -1
#define STACK_OVERFLOW -2

int main() {
    return 0;
}

StringStack* stack_create(unsigned int capacity) {
    StringStack* stack = (StringStack*)malloc(sizeof(struct stringstack));
    stack->items = (char**)malloc(sizeof(char*) * capacity);
    stack->capacity = validatedCapacity(capacity);
    stack->top = -1;
    return stack;
}

char* stack_pop(StringStack* stack) {
    validateSizeNotZero(stack);
    char* topElement = stack->items[stack->top--];
    updateCapacity(stack);
    return topElement;
}

void stack_push(StringStack* stack, char* newElement) {
    validateNotFull(stack);
    stack->items[++stack->top] = newElement;
    updateCapacity(stack);
}

char* stack_peek(StringStack* stack) {
    return stack->items[stack->top];
}

bool stack_is_empty(StringStack* stack) {
    return stack->top == -1;
}

void stack_destroy(StringStack* stack) {
    free(stack->items);
    free(stack);
}

void updateCapacity(StringStack* stack) {
    if(stack->capacity == stack->top + 1) {
        stack->items = realloc(stack->items, sizeof(char*) * stack->capacity * 2);
        stack->capacity *= 2;
    } else if(stack->top + 1 * 4 < stack->capacity) {
        stack->items = realloc(stack->items, sizeof(char*) * stack->capacity / 2);
        stack->capacity = stack->capacity / 2;
    }
}

void validateSizeNotZero(StringStack* stack) {
    if(stack_is_empty(stack)) {
        exit(STACK_UNDERFLOW);
    }
}

void validateNotFull(StringStack* stack) {
    if(stack->top + 1 == stack->capacity) {
        exit(STACK_OVERFLOW);
    }
}