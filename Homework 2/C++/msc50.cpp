#include <random>
#include <iostream>

using namespace std;

int main() {
    random_device seedGenerator;
    uniform_int_distribution<int> d20(1, 20);

    cout<<"d20 rolled: "<<d20(seedGenerator);

    return 0;
}