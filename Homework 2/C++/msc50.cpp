/*
 * Author: Kieran Ahn
 *
 * Standard: MSC50-CPP. Do not use std::rand() for generating pseudorandom numbers
 * Description: Using std::rand() can lead to predictable pseudorandom number 
 * generation, which is a possible weakness that attackers can exploit, such as
 * to impersonate users with a weak randomly-generated ID.
 */

#include <random>
#include <iostream>

using namespace std;

int main() {
    random_device seedGenerator;
    uniform_int_distribution<int> d20(1, 20);

    cout<<"d20 rolled: "<<d20(seedGenerator);

    return 0;
}