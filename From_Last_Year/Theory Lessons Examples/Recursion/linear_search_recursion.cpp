/*"""
LINEAR-SEARCH(A, x)
	return LINEAR-SEARCH(A, x, l, |A|)


LINEAR-SEARCH(A, x, l, r)
	if ell > r then
		return -1
		
	else if A[ell] == x then
		return ell
	else
		return LINEAR-SEARCH(A, x, ell+1, r)
*/

#include <iostream>
#include <vector>

using namespace std;

int linear_search (vector <int> A, int x , int ell, int r);

int linear_search(vector <int> A, int x){
    return linear_search(A, x , 0, A.size()-1);
}

int linear_search (vector <int> A, int x , int ell, int r){
    if (ell > r) return -1;
	
	else if (A[ell] == x) return ell;
		
	else return linear_search(A, x , ell+1, r);
}

	
int main(){

    vector <int> L = {1,2,3,4,5,6,7,8,9,10};

    cout << linear_search(L, 4) << endl;

}
