#ifndef STACK_H
#define STACK_H

#include <string>
#include <memory>

class StringStack {
    static const unsigned int DEFAULT_CAPACITY = 10;
    std::unique_ptr<std::unique_ptr<std::string>[]> frame;
    unsigned int capacity;
    unsigned int size;

    void validate(const bool condition, const std::string message);
    void validateSizeNotZero();
    void validateCanGrow();
    unsigned int validatedCapacity(unsigned int capacity);
    void updateCapacity();

    public:
    StringStack();
    StringStack(unsigned int userCapacity);
    void push(const std::string newElement);
    std::string pop();
    std::string peek();
    bool isEmpty();
};



#endif