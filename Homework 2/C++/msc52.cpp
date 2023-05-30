#include <iostream>
#include <string>
#include <random>

using namespace std;

string guessNumber() {
    random_device seedGenerator;
    uniform_int_distribution<int> oneThroughTen(1, 10);
    int choice = oneThroughTen(seedGenerator);
    int guess;
    cin>>guess;
    if(guess == choice) {
        return "Your guess was correct!";
    } else if (guess > 0 && guess < 11) {
        return "Your guess was incorrect!";
    } else {
        return "Remember: a NUMBER BETWEEN 1 and 10.";
    }
}

int main() {
    cout<<"I'm thinking of a number between 1 and 10. Can you guess it?"<<endl;
    string response;
    response = guessNumber();
    cout<<response;
    return 0;
}