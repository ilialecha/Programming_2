
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

int main() {
    map<char,int> x = { { 'a',1 },{ 'b',2 },{'c',0} };
    map<char,int>::iterator best
        = max_element(x.begin(),x.end(),[] (const pair<char,int>& a, const pair<char,int>& b)->bool{ return a.second < b.second; } );
    cout << best->first << " , " << best->second << "\n";
    return 0;
}
