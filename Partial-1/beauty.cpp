/*
function beauty(s)
    let D be an empty dictionary
    for i = 1 to |s| do
        x = s[i]
        if x in D then
            D[x] = D[x] + 1
        else
            D[x] = 1
    least = |s|
    most = 0
    for all x in D do
        if D[x] < least then
            least = D[x]
        if D[x] > most then
            most = D[x]
    return most − least
*/

#include <iostream>
#include <map>

using namespace std;

int beauty(string s){
    map<char, int> D;
    for (char c : s) ++D[c];

    int most = 0;
    int least = s.length();

    //for (auto it: D) cout << it.first << "-->"<<it.second;

    for (auto it: D){
        if (D[it.first] < least) least = D[it.first];
        if (D[it.first] > most) most = D[it.first];
    }

    
    return most - least;
}

int main(){

    string s = "abaabc";

    int exec = beauty(s);

    cout << exec <<endl;

    return 0;
}