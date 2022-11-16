#include <map>
#include <iostream>

using namespace std;


int beauty(string s){
    map<char,int>D;
    for(char i: s) 
        ++D[i];
    
    int low = s.size();
    int high = 0;
    
    for(auto it: D){
        if (it.second < low) low = it.second;
        if (it.second > high) high = it.second;
    }
    return high - low;
}

int sum_beauty(string s){
    int n = s.size();
    int r = 0;
    for (int i = 0; i<(n-1); i++){
        for (int j = i+1; j<n; j++){
            if (i<j) r = r + beauty(s.substr(i,j));
        }   
    }
    return r ;
}


int main(){


    cout << sum_beauty("aabcb") << endl;

    return 0;
}