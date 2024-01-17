#include<iostream>
using namespace std;
class Parent
{
	
	public:
		void mobile()
		{
			
			cout<<"Samsung s23 Ultra";
		}
};
class child : public Parent
{
	
	public:
		void mobile()
		{
			Parent :: mobile(); // using scope resolution operator
			cout<<"\nSamsung Galaxy";
		}
};
main(){
	
	
	child c1;
	c1.mobile();
}
