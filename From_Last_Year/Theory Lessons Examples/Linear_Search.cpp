#include <iostream>
#include <vector>

using namespace std;

int search(vector<int>V, int x){
for (int i = 0; i < V.size(); i++){  
      if (V[i] == x)
         return i;
         }
return -1;
}


int main(){
    int n = 10;
    vector<int> t(n,11);
    int res = search(t, n);

    cout << res << endl;

    return 0;
}


