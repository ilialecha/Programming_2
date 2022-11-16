#include <string>
#include <iostream>

using namespace std;

int count_a(string s, char c){
    int i = 0;
    int a = 0;
    bool found = false;
    while (i<s.length() &&  found==false){
        if (s.at(i) == c){
            found = true;
            break;
        }
        if (s.at(i)=='a') ++a;
        ++i;
    }
    if (found==true) return a;
    else return -1;
}

int main(){

    cout << count_a("naturally", 'u') << endl;
    cout << count_a("russian", 't') << endl;
    cout << count_a("adaptation", 'a') << endl;
    cout << count_a("adaptation", 'n') << endl;

    return 0;
}