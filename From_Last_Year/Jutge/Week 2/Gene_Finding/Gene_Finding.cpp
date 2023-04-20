#include <iostream>
#include <string>

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

string seq;
string res = "";

//input: GGTTTCTATGTGGCTAAATACGTTAACAAAAAGTCAGATATGGACCTTGCTGCTAAAGGTCTAGGAGCTAAAGAATGGAA
string gene_find(string seq){

    bool searching_start = 1;
    bool found_end = 0;

    int i = 0;
    
    while (searching_start == 1 and i < seq.length()-3 and seq.length() > 6){
        
        if (seq.substr(i,3) == "ATG"){
            res+=seq.substr(i,3);
            searching_start = 0;
            i+=3;
            break;
        }
    i++;
    }

    while (searching_start == 0 and i < seq.length()){
        
        res+=seq.substr(i,3);
        
        if(seq.substr(i,3) == "TAA" || seq.substr(i,3) == "TAG" 
        || seq.substr(i,3) == "TGA"){
            found_end = 1;
            break;
        }
        
        i+=3;
    }

    return res;
    /*
   if (found_end == 1){
       return res;
   }
   else{
       return "None";
   }*/
   
}


int main(){
    string seq;
    cin >> seq;

    cout << gene_find(seq) << endl;
    
    
    }
    
