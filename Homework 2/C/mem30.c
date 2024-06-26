/*
 * Author: Kieran Ahn
 * 
 * Standard: MEM30-C. Do not access freed memory
 * Description: Writing to, double freeing, or otherwise manipulating freed 
 * memory can cause all sorts of nasty side-effects and errors, such as 
 * crashes, execution of arbitrary code, data corruption, and more. Never 
 * access freed memory.
 */

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    if(argc != 2) {
        printf("Program requires 1 argument.");
        return 1;
    }
    const size_t rawMessageLength = strlen(argv[1]);
    
    if(rawMessageLength > 1000) {
        printf("Message is too long");
        return 1;
    }

    const size_t echoLength = rawMessageLength * 3 + 1;
    char* message = (char *)malloc(echoLength);
    
    if(!message) {
        printf("Unable to allocate memory.");
        return 1;
    }

    for(int i = 0; i < 3; i++) {
        strcpy(message + rawMessageLength*i, argv[1]);
    }
    
    printf(message);

    free(message);
}