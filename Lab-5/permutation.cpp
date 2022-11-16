#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> words(int n, vector<char>& A){

    sort(A.begin(), A.end ());
    vector<string> L;
    L.push_back("");

    for(int i = 0; i < n; ++i){

        vector<string> LL;
        for(auto s:L){
            for(auto x:A){
                LL.push_back({x+s});
            }
        }
        L = LL;
    }
    return L;
}


int main(){
    vector<char>A;
    int n; 
    cin >> n;
    char x;
    while(cin >> x) A.push_back(x);
    vector<string> result = words(n,A);
    for (auto a: result)cout << a << endl;
    return 0;
}