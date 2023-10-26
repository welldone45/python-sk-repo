#include<stdio.h>
main()
{
	
	int choice;
	
	printf("Enter your number (1,2 or 3..) \n\n");
	scanf("%d",&choice);
	
	switch(choice)
	{
		case 1:
		printf("you chose 1 \n");
		break;
		
		case 2:
			printf("you chose 2 \n");
			break;
			
		case 3:
			printf("you chose 3 \n");
			break;	
	}
		return 0;
	
}