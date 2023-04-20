#include <iostream>
#include <vector>

using namespace std;

int search(vector<int> A, int x){
    int n = A.size();
    if (n <= 0) return -1;
    A[0] = x;
    return 0;
}


int main(){
    vector<int> B(20, 0);
    int y = 5;
    int p = search(B,y);
    cout << (B[p] == y ? "True" : "False") << endl;

}