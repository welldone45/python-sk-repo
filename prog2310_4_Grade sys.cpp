#include<stdio.h>
main()
{


	int marks;
	
	printf("Enter Your Marks : \n");
	scanf("%d",&marks);
	
	if(marks>=0 && marks<=100)
	{
		if(marks>=0 && marks<=32)
		{
			printf("Fail");
			
		}
		else if(marks>=33 && marks<=50)
		{
			printf("C");
			
		}
		else if(marks>=51 && marks<=60)
		{
			printf("B");
		}
		else if(marks>=61 && marks<=70)
		{
			printf("A");
		}	

		else if(marks>=71 && marks<=100)
		{
			
			printf("A+");
		}
		else
		{
			
			printf("Invalid marks");
		}
	}

}