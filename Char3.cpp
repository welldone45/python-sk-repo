#include <stdio.h>

int main() {
    // Declare two character variables
    char firstchar[50];
    char secondchar[50];

    // Declare two integer variables
    int firstint;
    int secondint;

    // Print the values of the variables
    printf("Enter firstchar: \n");
	gets(firstchar);
    
    printf("Enter secondchar: \n");
	gets(secondchar);
    
	
	printf("Enter firstint: \n");
	scanf("%d",&firstint);

    printf("Enter Secondint: \n");
    scanf("%d",&secondint);

	printf("You have entered firstchar :%s \n You have entered secondchar : %s and You hv entered firstint is: %d \n You hv entered secondint is :%d",firstchar,secondchar,firstint,secondint);
    return 0;
}





