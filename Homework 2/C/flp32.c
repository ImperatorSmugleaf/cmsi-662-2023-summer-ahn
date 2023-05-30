#include <math.h>
#include <stdio.h>

int main() {
    printf("Please input a number and receive the log of that number.\n");
    double number;
    scanf("%lf", &number);
    if (islessequal(number, 0.0)) {
        printf("Log function is not defined for zero and below.");
    } else {
        printf("%lf", log(number));
    }
}