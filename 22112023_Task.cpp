#include<iostream>
using namespace std;
class company{
	
	public:
	int id;
	string name;
	string location; 
	float turnover;
	
	void inputdata(){
		
		cout<<"\n enter company id :";
		cin>>id;
		cout<<"\n enter company name :";
		cin>>name;
		cout<<"\n enter company turnover :";
		cin>>turnover;
		cout<<"\n enter company location :";
		cin>>location;
				
	}	
	
	void displaydata(){
		
		cout<<"company id"<<id;
		cout<<"company name"<<name;
		cout<<"company turnover"<<turnover;
		
	}
	
	};
	
class employee{
	
	public:
	int id;
	string name;
	string dept; 
	float sal;
	
	void inputdata(){
		
		cout<<"\n enter employee id :";
		cin>>id;
		cout<<"\n enter employee name :";
		cin>>name;
		cout<<"\n enter employee dept :";
		cin>>dept;
		cout<<"\n enter employee sal :";
		cin>>sal;
				
	}	
	
	void displaydata(){
		
		cout<<"employee id"<<id;
		cout<<"employee name"<<name;
		cout<<"employee dept"<<dept;
		cout<<"employee sal"<<sal;
		
	}
		
};	
	
main(){
	
	company cobj;
	cobj.inputdata();
	cobj.displaydata();
	
	employee eobj;
	eobj.inputdata();
	eobj.displaydata();
	
	
	
}