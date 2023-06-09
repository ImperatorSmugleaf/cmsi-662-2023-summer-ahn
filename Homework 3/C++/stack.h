#ifndef STACK_H
#define STACK_H

#include <string>

class StringStack {
    public:
    StringStack();
    StringStack(unsigned int userCapacity);
    void push(const string newElement);
    string pop();
    string peek();
    bool isEmpty();
};



#endif