#include <errno.h>
#include <float.h>
#include <stdlib.h>
#include <stdio.h>

int main() {
    double userNumber;
    char* endOfString;
    char stringToParse[101];

    printf("Please input a floating point number to parse!\n");
    scanf("%100s", &stringToParse);

    userNumber = strtod(stringToParse, &endOfString);

    if (endOfString == stringToParse) {
        fprintf(stderr, "%s is not a valid float.\n", stringToParse);
    } else if ('\0' != *endOfString) {
        fprintf(stderr, "%s is not a single floating point value. Please provide only a floating point value.\n", stringToParse);
    } else if ((DBL_MIN == userNumber) || (DBL_MAX == userNumber) && ERANGE == errno) {
        fprintf(stderr, "%s is out of range of type double.\n", userNumber);
    } else if (userNumber > FLT_MAX) {
        fprintf(stderr, "%lf is greater than FLT_MAX.\n", userNumber);
    } else if (userNumber < FLT_MIN) {
        fprintf(stderr, "%lf is less than FLT_MIN.\n");
    } else {
        fprintf(stdout, "Your float is: %f", userNumber);
    }

    return 0;
}