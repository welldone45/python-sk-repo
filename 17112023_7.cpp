#include <stdio.h>

int main() {
    int score;

    printf("Enter your score (0-100): ");
    scanf("%d", &score);

    switch (score) {
        case 90 ... 100:
            printf("You got an A!\n");
            break;
        case 80 ... 89:
            printf("You got a B.\n");
            break;
        // ... more cases ...
        default:
            printf("Invalid score.\n");
    }

    return 0;
}