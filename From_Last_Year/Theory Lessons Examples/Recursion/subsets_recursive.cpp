#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector <vector <string>> subsets (const vector <string>& S){

    vector <vector < string>> L;
    int n = S.size();

    if (n == 0){
        L.push_back({});
    }

    else {

        vector <string> SS(S);
        SS.erase(SS.begin());

        for(vector <string> X : subsets(SS)){
            L.push_back(X);
            vector <string> Y(X);

            Y.push_back(S[0]);
            L.push_back(Y);
        }

    }

for(auto i = L.begin(); i != L.end(); i++) 
    sort((*i).begin(), (*i).end());

sort(L.begin(), L.end());

return L;
}

int main(){

    vector<string> S = {"A", "B", "C"};

    vector <vector<string>> L = subsets(S);

    for (auto X : L){
        for(auto x : X) cout << x << " ";
            cout << endl;
        
    }
}