#include <vector>
#include <iostream>
using namespace std;

int binary_search(vector<int> a, int low, int high, int x){

    while (low <= high){
        int mid = (low+high)/2;
        if (a.at(mid) == x)
            return mid;
        else if (x > a.at(mid))
            low = mid + 1;
        else
            high = mid - 1;
    }

    return -1;
}


int main() {

    vector<int> a = {1,2,3,4,5,6,7,8,9,10};
    int low = 2;
    int high = 9;

    int bs = binary_search(a,low,high,4);

    cout << "4 is at position: " << bs << endl;
    
    return 0;
}