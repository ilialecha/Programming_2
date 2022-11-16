#include<iostream>

using namespace std;


int main(){
    int matrix[3][3] = {{1,1,1},{2,2,2},{3,3,3}};
    int diag[3];
    int index = 0;
    for (int i = 0;i<3;i++){
        for (int j = 0;j<3;j++){
            if (j == i)
            {
                diag[index] = matrix[i][j];
                index++;
                cout<<"Elem. = "<<matrix[i][j];
                cout<<"\n";
            }
            
        }   
    }
    return 0;
}