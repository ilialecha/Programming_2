#include <iostream>
#include <vector>

using namespace std;

void InsSort(vector<int>& A){
	
	for (int j = 1; j < A.size(); ++j){
		int k = A[j];
		int i = j-1;
		
		while (i >= 0 and A[i] > k){
			
			A[i+1] = A[i];
			i = i-1;
			}
			
			A[i+1] = k;
		}
	}

int main(){
	
	vector<int> A = {5,2,4,6,1,3};
	
	for (auto  i: A) cout << i << " ";
	cout << endl;
	
	InsSort(A);
	
	for (auto  i: A) cout << i << " ";
	cout << endl;
	
	}
