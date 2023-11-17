#include<stdio.h>
main(){


	int marks;
	
	printf("enter your marks \n");
	scanf("%d",&marks);
	
	if(marks>=0 && marks<35){
		
		printf("fail");
	}
	else if(marks>=35 && marks<=50){
		
		printf("C Class");
	}
	else if(marks>=51 && marks<=59){
		
		printf("B Class");
	}	
	else if(marks>=61 && marks<=69){
	
		printf("A Class");
	}

	else if(marks>=70 && marks<=100){
	
		printf("Distinction");
	}
	else{
		
		printf("fail");
	}

}