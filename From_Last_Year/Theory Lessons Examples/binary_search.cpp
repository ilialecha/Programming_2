/*"""
binary-SEARCH(A, x)
	return binary-SEARCH(A, x, l, |A|)


binary-SEARCH(A, x, l, r)
	if ell > r then
		return -1
		
	else if A[ell] == x then
		return ell
	else
		return binary-SEARCH(A, x, ell+1, r)
*/

#include <iostream>
#include <vector>

using namespace std;

int binary_search (vector <int> A, int x , int ell, int r);

int binary_search(vector <int> A, int x){
    return binary_search(A, x , 0, A.size()-1);
}

int binary_search (vector <int> A, int x , int ell, int r){
    if (ell > r) return -1;
	
	else{
        int m = (ell+r) / 2;

        if(x < A[m]) return binary_search(A, x, ell, m-1);
        else if(x > A[m]) return binary_search(A, x, m+1, r);
        else return m;
    }
}

	
int main(){

    vector <int> L = {1,2,3,4,5,6,7,8,9,10};

    cout << binary_search(L, 4) << endl;

}
