#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;


int main(){
    float x;
    cin >>  x;
    int z;
    vector<int> v;

    while (cin >> z) v.push_back(z);

    float r=0.0;
    int j = 0;
    for (int i: v){
        r = r + (float)(i*pow(x,j));
        ++j;
    }
    cout << setprecision(5) << (float)r << endl;
}