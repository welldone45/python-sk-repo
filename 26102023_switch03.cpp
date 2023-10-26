#include<stdio.h>
main()

{
	int Grade;
	
	printf("enter your Grade (0-100)\n");
	scanf("%d",&Grade);
	
	if(Grade<0 || Grade>100){
		printf("invalid grade \n");
		
	}
	else
	{
		switch(Grade/10){
			case 10:
			case 9:
			case 8:
			case 7:	
				printf("your Grade is Distiction \n\n");
				printf("-:: CONGRATULATIONS : : - \n");
				break;
			case 6:
				printf("your letter grade is B\n\n");
				printf("Try little Hard\n");
				break;
			case 5:
				printf("your letter grade is C\n\n");
				printf("Try Hard\n");
				break;
			default:
				printf("fail\n\n");
				printf("Zindagi ki yahi reet hai har ke bad hi Jeet hai\n\n");
				break;
		}		
		
	}
	


}