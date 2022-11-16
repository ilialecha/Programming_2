#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

int max_of_seq(string myString){
    int sep = myString.find(" ");
    stringstream iss( myString.substr(sep) );

    int number;
    vector<int> T;
    while ( iss >> number )
    T.push_back( number );

    for ( int i=0; i < T.size()-1; ++i) 
        for ( int j = T.size()-1; j>i ; --j ) 
            if ( T[j] > T[j-1]) swap ( T[j] , T[j-1]); 
    
    return T.at(0);
}


int main(){


    /*int s;
    vector<int>v;
    cin >> s;

    for (int i=0;i<s;++i){
        if(cin>>s)
            cout << s << '\n';
        else
            break;
        cin>>s;

        v.push_back(s);
    }

    for (auto it:v) cout << it << endl;

    return 0;*/
}