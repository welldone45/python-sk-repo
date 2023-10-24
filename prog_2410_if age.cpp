#include<stdio.h>

main(){

	int age;
	char name;
	
	printf("Enter the Year : \n");
	scanf("%d",&age);
	
	if(age>=1550 && age<=1625){
		printf("The Elizabethan Age or The Age of Shakespeare");
	}
	else if(age>=1625 && age<=1660){
		printf("The Puritan Age or The Age of Milton");
	}	
	else if(age>=1661 && age<=1700){
		printf("The Age of Dryden or The Restoration Age");
	}
	else if(age>=1701 && age<=1740){
		printf("The Age of Pope or The Age of Augustan");
	}
	else if(age>= 1741 && age<=1798){
		printf("The Age of Johnson or The Age of Transition");
	}
	else if(age>=1799 && age<=1832){
		printf("The Age of Wordsworth or The Romantic Age");
	}
	else if(age>=1833 && age<=1890){
		printf("The Age of Tennyson or The Victorian Age");
	}
	else if(age>=1891 && age<=1918){
		printf("The Age of Thomas Hardy");
	}
	else if(age>=1919 && age<=1939){
		printf("The Age of Inter war year");
	}
	else if(age>=1940 && age<=1960){
		printf("The Modern Age");
	}		
	else{
		printf("no age");
	}
		
}	

