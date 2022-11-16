#include <strings.h>
#include <vector>
#include <iostream>

using namespace std;

/*
Pseudocode

function sliding_window_2(s,x,y):
    if |s| > x then
        let L be an empty list
        append s [1,...,x ] to L
        concatenate SLIDING-WINDOW(s [y + 1 : |s |],x ,y ) to L
    else
        return an empty list
*/

vector<string> sliding_window_2(string s, int x, int y){
    vector<string> L ;
    if (s.length() < x){
        return L;
    }else{
        L.push_back(s.substr(0,x));
        vector<string> LL = sliding_window_2(
            s.substr(y,s.length()-y),x,y
        );
        L.insert(L.end(),LL.begin(),LL.end());
        return L;
    }


}

int main(){
    string s;
    int x,y;
    cin >> s >> x >> y;
    vector<string> L = sliding_window_2(s,x,y);
    for (string s:L) cout << s << endl;
    return 0 ;
}