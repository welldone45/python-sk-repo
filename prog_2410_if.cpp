#include<stdio.h>
main(){

	int score;
	
	printf("Enter the Student's score : \n'");
	scanf("%d",&score);
	
	if(score>90){
		printf("Grade A \n");
	} 
	else if (score>=80){
		printf("Grade A  \n" );
	}
	else if(score>=70){
		printf("Grade B");
	}
	else if (score>=60){
		printf("Grade C");
	}
	else {
		printf("Fail");
	}
		
	return 0;

}
