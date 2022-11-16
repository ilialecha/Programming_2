#include <iostream>
#include <vector>

using namespace std;


int main(){

    //Read int i followed by i numbers
    int p = 0;
    while(cin>>p){
        for (int i=0;i<p;i++){
            int num =0;
            cin >> num;
            cout << num << endl;
        }
    }

    //Read uknown number of n
    int n;
    while (cin >> n){
        cout << n << endl;
    }

    //Read a and uknown number of b
    int x = 0;
    cin >> x;
    int z;
    vector<int> v;
    while (cin >> z) v.push_back(z);



}