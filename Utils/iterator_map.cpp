#include <vector>
#include <iostream>
#include <sstream>

using namespace std;

void iterate_vector(){
        vector<int> myNumbers;
        for ( int p : myNumbers ) cout << p << '\t' << p << std::endl;        
}

void iterate_map(){
        vector<int> myNumbers;
        for ( int p : myNumbers ) cout << p << '\t' << p << std::endl;        
}

int main(){
        return 0;
}

/*
for(it = ll.begin() ; it != ll.end(); ++it)
        cout << it->first << " " << it->second<<endl;
*/