#include<stdio.h>
main(){



	char week;
	scanf("%s",&week);
	switch(week){
	
		case 'm':
			printf("Monday");
			break;
		
		case 't':
			printf("Tuesday");
			break;
		case 'w':
			printf("Wednesday");
			break;
		case 'th':
			printf("Thursday");
			break;
		case 'f':
			printf("Friday");
			break;
		case 's':
			printf("Saturday");
			break;
		default: 
			printf("enter valid choice");
	
	}


}