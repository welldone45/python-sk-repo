#include<stdio.h>
main()
{
				
		float marks;
		float total=0;
		float percentage;
		
		printf("enter your marks (Math) :\n");
		scanf("%f",&marks);
		total = total + marks;
		
		printf("enter your marks (Sci) : \n");
		scanf("%f",&marks);
		total = total + marks;

		printf("enter your marks (Eng) : \n");
		scanf("%f",&marks);
		total = total + marks;
		
		printf("Total is %1f\n",total);
		
		percentage = (total*100)/5;
		printf("your grade is : %1f\n",percentage);

}

