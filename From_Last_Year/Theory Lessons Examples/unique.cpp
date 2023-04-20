#include <set>
#include <vector>
#include <iostream>

using namespace std;

bool unique(const vector <string> L){

    set <string> X;
    string x;

    for (auto x : L){
        if (x.find(x) == x.end()) x.insert(x);
        else return false; //find true if not in there
    }

    return true;
    
}

int main(){
    vector <string> L;
    string x;

    while(cin >> x){
        L.push_back(x);
    }
    bool found = unique(L);
    cout << (found ? "True" : "False") << endl;
}


