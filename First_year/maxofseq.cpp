#include <iostream>

using namespace std;

void maxofseq(){
    int x;
    int m = -1;
    while(cin >> x){
        for(int i=0; i<x;++i){
            int n;
            cin >> n;
            if (m==-1) m = n;
            if (n > m) m=n;
        }
    cout << m << endl;
    m=0;
    }
    
}

int main(){
    maxofseq();
    return 0;
}