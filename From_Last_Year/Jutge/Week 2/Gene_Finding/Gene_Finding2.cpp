#include <iostream>
#include <string>
//GGTTTCTATGTGGCTAAATACGTTAACAAAAAGTCAGATATGGACCTTGCTGCTAAAGGTCTAGGAGCTAAAGAATGGAA
using namespace std;
/*
GENE_FINIDING PSEUDOCODE:

searching_start <- True
end_found <- False

res = ""

i <- 0

while searching_start  and i < |seq|-3 do
	if seq[i:i+3] == "ATG" then
		res += seq[i:i+3]
		searching_start <- False
		i+=2
	i+=1
	
while searching_start is False and i < |seq|-3 do
	res += seq[i:i+3]
	
	if seq[i:i+3] == "TAA" or "TAG" or "TGA" then
		found_end <- True
		break
	i+=3

if found_end then
	return res

else:
	return nil
*/

string gene_find(string seq){

    int it = 0;
    int each3 = 0;

    string res = "";

    bool start = 0;
    bool end = 0;

    for(int i = 0; i < seq.length()-2; i++) {
         
        if (seq.substr(i,3) == "ATG" && start == 0){

            res += seq.substr(i,3);
            it = i+3;
            start = 1;  
        }
    
    while(start == 1 && end == 0){
           
        for(it; i < seq.length()-2; i++){
            //cout << it << endl;
            //cout << seq.substr(it,3) << endl;  
            if(seq.substr(it,3) == "TAA" || 
               seq.substr(it,3) == "TAG" || 
               seq.substr(it,3) == "TGA"){
                   
                   res += seq.substr(it,3);
                   end = 1;
                   break;
               }
               
            else{
                res += seq.substr(it,3);
                each3 += 3;

                if(each3%3 == 0){
                    it += 3;
                   }
               
               }
                
           }
           if(end == 0){
               break;
           }   
       }
    }
    return res;
}

int main(){

    string seq;
    cin >> seq;

    cout << gene_find(seq) << endl;
}