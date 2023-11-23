#include<iostream>
using namespace std;
class fact{
	
	public:
		
		void inputdata(){
		
		int num;
		cout<<"enter the number : ";
		cin>>num;
			
		}
		
		void displaydata(){
			
		cout<<"factorial val is : "<<num;

		}

};

main(){
	
	int num;
	fact fobj;
	fobj.inputdata();
	fobj.displaydata();
}