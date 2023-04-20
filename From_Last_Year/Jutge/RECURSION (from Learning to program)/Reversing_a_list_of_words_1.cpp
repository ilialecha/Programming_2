#include <vector>
#include <string>
#include <iostream>

using namespace std;

void printReversed(int * x)
{
    if (*x == 0) return;

    cout << *x;
    printReversed(x+1);
    cout << *x;
}


int main(){

    string s;
    vector <string> l;
    vector <string> l2;

    while(cin >> s){
        l.push_back(s);
    }

   
   

    for(int i = l.size() -1 ; i >= 0 ; i--){
        cout << l[i] << endl;
    }

    

}
