#include<stdio.h>
#include<conio.h>
main()

{
	
	
	char name[50];
	char city[50];
	int age;
	float marks;
	
	printf("Enter your name : \n");
	gets(name);
	printf("Your name is : %s",name);
	
	printf("\n Enter our age :\n");
	scanf("%d",&age);
	printf("Your Age is : %d",age);
	
	fflush(stdin);
	printf("\n Enter your city :\n");
	gets(city);
	printf("Your City is :%s",city);
	
	printf("\n Enter your marks :");
	scanf("%f",&marks);
	printf("Marks You obtained : %f",marks);
	
	
		
	
	
	
	
}

