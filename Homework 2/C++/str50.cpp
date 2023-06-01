/*
 * Author: Kieran Ahn
 * 
 * Standard: STR50-CPP. Guarantee that storage for strings has sufficient space
 * for character data and the null terminator
 * Description: Following this standard ensures that attackers cannot execute
 * a buffer overflow attack through the unprotected string.
 */

#include <iostream>
#include <string>

using namespace std;

int main() {
    cout<<"Please type something for me to echo!"<<endl;
    string echo;
    cin>>echo;
    cout<<echo<<" "<<echo<<" "<<echo;

    return 0;
}