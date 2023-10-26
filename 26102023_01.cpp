#include<stdio.h>
main(){


	char name[50];
	float marks;
	float total;
	
	printf("enter your name : \n\n");
	gets(name);
	
	printf("enter your makrs :\n\n");
	scanf("%f",&marks);
	total = total + marks; 
	scanf("%f",&marks);
	total = total + marks;
	scanf("%f",&marks);
	total = total + marks;
	scanf("%f",&marks);
	total = total + marks;
	scanf("%f",&marks);
	total = total + marks;

	float percentage;
	printf("your total marks : %.2f \n\n",total);
	percentage = (total*100)/500;
	
	printf("your percentage is : %.2f \n\n",percentage);
	
}

