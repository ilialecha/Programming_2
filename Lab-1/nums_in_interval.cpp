#include <iostream>
using namespace std;

/*
procedure num_in_interval(a,b)
    if a <= b then
        for i=a up to b do
            if i != b then
                output i without new line
            else
                output i with new line
    else
        output an empty line
*/

void nums_in_interval(int a, int b){
    if (a <= b){
        for (int i=a; i<=b ;++i){
            if (i != b) cout << i << ",";
            else cout << i << endl;
        }
    }else{
        cout << endl;
    }
}

int main(){

    int a,b;
    cin >> a;
    cin >> b;

    nums_in_interval(a,b);
    return 0;
}