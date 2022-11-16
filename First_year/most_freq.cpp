#include <iostream>
#include <unordered_map>

using namespace std;

int main(){
    char c;
    int n = 0;
    pair<char,int> output = {' ',0};
    unordered_map<char,int> D;
    while(cin>>c){
        if (isalpha(c) && islower(c))++D[c];
    }
    for(auto const& x:D) if (x.second > output.second) output = make_pair(x.first,x.second);

    cout << output.first << " " << output.second << endl;
    return 0;
}