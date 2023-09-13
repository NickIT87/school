#include <stdio.h>
#include <stdlib.h>

#define esc 27

int main()
{
    char ch;
    int exitflag = 0; // Initialize exitflag to 0

    do
    {
        ch = getchar(); // Use getchar() to read a character
        switch(ch)
        {
            case esc:
                printf("Escape key pressed. Exiting program.\n");
                exitflag = 1;
                break;
        }
    }
    while(exitflag != 1);

    return 0; // Return 0 to indicate successful execution
}
