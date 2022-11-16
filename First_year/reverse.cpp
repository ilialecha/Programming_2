#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> v = {1,2,3,4,5,6,6,7,8};
    int size = v.size()-1;
    for(int i=size;i>=0;--i) cout << v.at(i) << endl;
}