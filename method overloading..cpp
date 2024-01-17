#include<iostream>
using namespace std;
class overloadingDemo
{
	
	public:
		void addition(int a,int b)
		{
			
			cout<<a+b<<endl;
		}
		void addition(float a,float b)
		{
			
			cout<<a+b<<endl;
		}	
		void addition(int a,int b,int c)
		{
			
			cout<<a+b+c<<endl;
		}
};
main(){
	
	
	overloadingDemo od;
	od.addition(10,20);
	od.addition(56.34f,24.54f);
	od.addition(5,6,7);
}