#include <iostream>
#include <unordered_map>

using namespace std;

int main(){


    int n,nn;
    int r = 0;
    unordered_map<int,int> D;
    
    cin >> n;
    for(int i = 1; i<=n; ++i){
        cin >> nn;

        if( i==n && D.count(nn)>0 ) r = D[nn];
        else ++D[nn];
    }
    cout << r << endl;
}