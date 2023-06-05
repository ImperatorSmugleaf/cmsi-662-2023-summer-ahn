#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct stringstack {
    unsigned int capacity;
    unsigned int size;
    char** frame;
} StringStack;

StringStack* makeStringStack();
void push(StringStack* stack, char* newElement);
char* pop(StringStack* stack);
void validateCapacity(StringStack* stack);
void validateSizeNotZero(StringStack* stack);


int main() {
    return 0;
}

StringStack* makeStringStack() {
    StringStack* stack = (StringStack*)malloc(sizeof(struct stringstack));
    stack->frame = malloc(sizeof(char*) * 10);
    stack->capacity = 10;
    stack->size = 0;
    return stack;
}

char* pop(StringStack* stack) {
    //TODO: check if stack is empty
    char* topElement = stack->frame[stack->size - 1];
    stack->size--;
    return topElement;
}

void push(StringStack* stack, char* newElement) {
    //TODO: check if stack exceeds capacity, and update if so
    stack->frame[stack->size] = newElement;
}