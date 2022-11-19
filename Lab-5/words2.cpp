#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> words(int n, vector<char>& a){
    sort(a.begin(),a.end());
    vector<string> L;
    if (n==0) L.push_back("");
    else{
        vector<string> W = words(--n,a);
        for (auto w:W){
            for (auto x:a)
                L.push_back(w+x); 
        }}return L;

}

int main(){
    string s;
    getline(cin,s);
    int n = stoi(s);
    vector<char> a;
    char a_i;
    while (cin >> a_i) a.push_back(a_i);

    for (auto w: words(n,a)) cout << w <<endl;

    return 0;
}