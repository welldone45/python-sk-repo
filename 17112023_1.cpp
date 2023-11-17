#include<stdio.h>
main(){


	int age;
	char city[50],name[50];
	float marks;


	printf("enter your name\n");
	scanf("%s",&name);
		
	fflush(stdin);
	printf("\nenter your city\n");
	scanf("%s",&city);
		

	printf("\nenter your age\n");
	scanf("%d",&age);
	
	printf("\nenter your marks\n");
	scanf("%1f",&marks);
		

	printf("\nyour name is : %s\n",name);
	printf("\nyour city is : %s\n",city);
	printf("\nyour age is: %d\n",age);
	printf("\nyour age is: %1f\n",marks);

}