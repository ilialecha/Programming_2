#include <regex>
#include <iostream>

using namespace std;

int main()
{
    const string s = "GGTTTCTATGTGGCTAAATACGTTAACAAAAAGTCAGATATGGACCTTGCTGCTAAAGGTCTAGGAGCTAAAGAATGGAA";
    
    regex TAA("ATG(\\D*)TAA");
    regex TAG("ATG(\\D*)TAG");
    regex TGA("ATG(\\D*)TGA");
    
    smatch match;

    string temp1, temp2, temp3;
    

    if (regex_search(s.begin(), s.end(), match, TAA))
        temp1 = "ATG" + match[1].str() + "TAA" + "\n";
        


    if (regex_search(s.begin(), s.end(), match, TAG))
        temp2 = "ATG" + match[1].str() + "TAG" + "\n";
        

    if (regex_search(s.begin(), s.end(), match, TGA))
        temp3 = "ATG" + match[1].str() + "TGA" + "\n";


    int l1 = temp1.length();
    int l2 = temp2.length();
    int l3 = temp3.length();


    if (l1 == 0)
    l1 = l2+l3+1;

    if (l2 == 0)
    l2 = l1+l3+1;

    if (l3 == 0)
    l3 = l2+l1+1;


    if ((l1 < l2) && (l1 < l3)) 
    {
        cout << temp1;
    }
    
    if ((l2 < l1) && (l2 < l3))
    {
        cout << temp2;
    }

    if ((l3 < l2) && (l3 < l1))
    {
        cout << temp3;
    }
}       

