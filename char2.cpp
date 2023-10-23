#include <stdio.h>

int main() {
    char name[50];
    char city[100];
    int marks;
    int age;

    printf("Enter your name: \n");
    fgets(name, sizeof(name), stdin);

    printf("Enter your age: \n");
    scanf("%d", &age);

    // Consume the newline character left in the input buffer
    while (getchar() != '\n');

    printf("Enter your city: \n");
    fgets(city, sizeof(city), stdin);

    printf("Enter your marks: \n");
    scanf("%d", &marks);

    printf("Your name is: %s\nYour age is: %d\nYour city is: %s\nMarks are: %d\n", name, age, city, marks);

    return 0;
}