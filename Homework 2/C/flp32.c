/*
 * Author: Kieran Ahn
 * 
 * Standard: FLP32-C. Prevent or detect domain and range errors in math functions
 * Description: You must always perform bounds checking on any value passed to
 * a C math function to ensure that it is within the domain of the function,
 * otherwise it will return bad data.
 */

#include <math.h>
#include <stdio.h>

int main() {
    printf("Please input a number and receive the log of that number.\n");
    double number;
    scanf("%lf", &number);
    if (islessequal(number, 0.0)) {
        printf("Log function is not defined for zero and below.");
    } else {
        fprintf(stdout, "%lf", log(number));
    }
}