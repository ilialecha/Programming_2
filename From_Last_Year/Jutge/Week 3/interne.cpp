#include <iostream>
#include <string>

using namespace std;

void codon (string);

int main()
{
 char Adenine = 'A';
 char Guanine = 'G';
 char Cytosine = 'C';
 char Thymine = 'T';
 string strand;

 cout << "Please input your DNA:" << endl;
 cin >> strand;
 cout << "This is the RNA sequence your entered: " <<strand << endl;
 codon(strand);

 system ("PAUSE");
 return 1;
}

void codon (string start)
{
	int tryptophan = 0;
	string::size_type aug_pos = start.find("AUG");
if(aug_pos != string::npos)
{
  cout << "The coding region starts at position " << aug_pos + 1 << endl;
  string::size_type ugg_pos = start.find("UGG", ugg_pos + 3);
  string::size_type uag_pos = start.find("UAG", aug_pos + 3);
  if(ugg_pos != string::npos)
  {
    tryptophan++;
	cout << tryptophan << endl;
  }
  else if(aug_pos != string::npos)
	  cout << "The coding region ends at position " << uag_pos + 1 << endl;
}
else
  cout << "Could not find the codon region..." << endl;
}