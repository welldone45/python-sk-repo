#include<stdio.h>
main(){
	
	
	char name[100];
	int age,choice;
	
	printf("enter your name: \n\n");
	gets(name);
	
	printf("enter your age :\n\n");
	scanf("%d",&age);
	
	printf("you name is : %s \n\n",name);
	printf("your age is : %d \n\n",age);
	
	printf("enter your role : \n 1) Batsman 2) Bowler 3) All Rounder");
	scanf("%d",&choice);
	
	if(choice==1){

		printf("\n you are a Batsman",name);
		
		int runs,wicketlost;
		
		printf("\n enter your runs : \n");
		scanf("%d",&runs);
		printf("\n number of time you lost wicket");
		scanf("%d",&wicketlost);
		
		float avg;
		
		avg = runs/wicketlost;
		printf("\n your average is : %.2f",avg);

	}	
	
	
}