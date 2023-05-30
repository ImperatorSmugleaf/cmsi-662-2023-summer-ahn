#include <math.h>
#include <stdio.h>

int main() {
    printf("Please input a number and receive the log of that number.\n");
    double number;
    scanf("%lf", &number);
    if (isless(number, 0.0)) {
        printf("Log function is not defined for numbers below 0.");
    } else if (number == 0.0) {
        printf("infinity");
    } else {
        printf("%lf", log(number));
    }
}