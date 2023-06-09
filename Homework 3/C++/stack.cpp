#include <algorithm>
#include <iostream>
#include "stack.h"

using namespace std;

void StringStack::validate(const bool condition, const string message) {
    if(!condition) {
        cout<<message<<endl;
        throw;
    }
}

void StringStack::validateSizeNotZero() {
    StringStack::validate(this->size > 0, "Stack size must be greater than 0.");
}

void StringStack::validateCanGrow() {
    StringStack::validate(UINT_MAX - this->capacity > UINT_MAX - this->capacity * 2, "Maximum capacity reached.");
}

unsigned int StringStack::validatedCapacity(const unsigned int capacity) {
    StringStack::validate(capacity > 0, "Capacity must be greater than 0.");
    return capacity;
}

void StringStack::updateCapacity() {
    unsigned int newCapacity = -1;
    if(this->capacity >= this->size) {
        StringStack::validateCanGrow();
        unsigned int newCapacity = this->capacity * 2;
    } else if (this->size * 4 <= this->capacity) {
        unsigned int newCapacity = this->capacity / 2;
    } else {
        return;
    }

    auto newFrame = make_unique<unique_ptr<string>[]>(newCapacity);
    for(int i = 0; i < this->size; i++) {
        newFrame[i].swap(this->frame[i]);
    }
    this->capacity = newCapacity;
    this->frame.swap(newFrame);
}

StringStack::StringStack() {
    this->frame = make_unique<unique_ptr<string>[]>(StringStack::DEFAULT_CAPACITY);
    this->capacity = DEFAULT_CAPACITY;
    this->size = 0;
}

StringStack::StringStack(unsigned int userCapacity) {
    this->frame = make_unique<unique_ptr<string>[]>(StringStack::validatedCapacity(userCapacity));
    this->capacity = userCapacity;
    this->size = 0;
}

void StringStack::push(const string newElement) {
    this->frame[this->size] = make_unique<string>(newElement);
    size++;
    StringStack::updateCapacity();
}

string StringStack::pop() {
    StringStack::validateSizeNotZero();
    size--;
    string topElement = *this->frame[this->size].release();
    StringStack::updateCapacity();
    return topElement;
}

string StringStack::peek() {
    return *this->frame[this->size-1].get();
}

bool StringStack::isEmpty() {
    return this->size==0;
}

int main() {
    printf("Existence\n");
    StringStack myDefaultStringStack;
    StringStack mySpecialStringStack(100);
    printf("Still here\n");
    myDefaultStringStack.push("Amogus");
    myDefaultStringStack.push("Sus");
    mySpecialStringStack.push("Aaaaaa");
    printf("Yeah\n");
    mySpecialStringStack.pop();
    cout<<myDefaultStringStack.pop()<<endl;
    cout<<myDefaultStringStack.peek()<<endl;
    return 0;
}