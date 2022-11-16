#include <iostream>

using namespace std;


int main(){

   
    int p = 0;

    while(cin>>p){
        for (int i=0;i<p;i++){
            int num =0;
            cin >> num;
            cout << num << endl;
        }
    }


}


/*
int n = 1234;
//Convert int to string
cout << to_string(n).length() << endl;

//Convert string to int.
string ns = "1234";
int nsn = stoi(ns);

//Run through a string
for (char c : ns) cout << c <<endl;

*/