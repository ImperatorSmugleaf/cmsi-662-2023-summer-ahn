#include <string>
#include <algorithm>
#include <iostream>
#include <memory>

using namespace std;

class StringStack {
    static const unsigned int DEFAULT_CAPACITY = 10;
    unique_ptr<unique_ptr<string>[]> frame;
    unsigned int capacity;
    unsigned int size;

    void validate(const bool condition, const string message) {
        if(!condition) {
            cout<<message<<endl;
            throw;
        }
    }

    void validateSizeNotZero() {
        validate(this->size > 0, "Stack size must be greater than 0.");
    }

    void validateCanGrow() {
        validate(UINT_MAX - this->capacity > UINT_MAX - this->capacity * 2, "Maximum capacity reached.");
    }

    unsigned int validatedCapacity(const unsigned int capacity) {
        validate(capacity > 0, "Capacity must be greater than 0.");
        return capacity;
    }

    void growCapacity() {
        if(this->capacity == this->size) {
            validateCanGrow();
            unique_ptr<unique_ptr<string>[]> newFrame(new unique_ptr<string>[this->capacity * 2]);
            for(int i = 0; i < this->size; i++) {
                newFrame[i].swap(this->frame[i]);
            }
            this->capacity = this->capacity * 2;
            this->frame.swap(newFrame);
        }
    }

    public:
    StringStack() {
        this->frame = unique_ptr<unique_ptr<string>[]>(new unique_ptr<string>[DEFAULT_CAPACITY]);
        this->capacity = DEFAULT_CAPACITY;
        this->size = 0;
    }

    StringStack(unsigned int userCapacity) {
        this->frame = unique_ptr<unique_ptr<string>[]>(new unique_ptr<string>[validatedCapacity(userCapacity)]);
        this->capacity = userCapacity;
        this->size = 0;
    }

    void push(const string newElement) {
        this->frame[this->size] = unique_ptr<string>(new string(newElement));
        size++;
        growCapacity();
    }

    string pop() {
        validateSizeNotZero();
        size--;
        return *this->frame[this->size].release();
    }

    string peek() {
        return *this->frame[this->size-1].get();
    }
};

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