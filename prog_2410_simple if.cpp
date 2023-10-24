#include<stdio.h>

main()
{

	int number;
	
	printf("Enter Your Numberr :\n");
	scanf("%d",&number);
	
	if(number>0){

		printf("The Number is Positive.\n");

	}

	else if (number<0){

		printf("The Number is Negative.\n");

	}

	else{
		
		printf("The Number is Zero.\n");
	}
	
	return 0;
	}


	