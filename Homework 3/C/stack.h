#ifndef STACK_H
#define STACK_H

#include <stdbool.h>

typedef struct stringstack {
    unsigned int capacity;
    int top;
    char** items;
} StringStack;

StringStack* stack_create(int capacity);
void stack_push(StringStack* stack, char* newElement);
char* stack_pop(StringStack* stack);
char* stack_peek(StringStack* stack);
void stack_destroy(StringStack* stack);
bool stack_is_empty(StringStack* stack);
int validatedCapacity(int capacity);
void validateSizeNotZero(StringStack* stack);
void validateNotFull(StringStack* stack);
void updateCapacity(StringStack* stack);
void validateCanGrow(int capacity);


#endif