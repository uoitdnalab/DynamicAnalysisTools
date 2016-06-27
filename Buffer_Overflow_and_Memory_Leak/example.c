#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	printf(“Hello, World!\n”);
	printf(“Let’s try to allocate memory.\n”);
	char *buf = (char *)malloc(4);
	strcpy(buf,”Hello, World!”); //Here’s where the overflow occurs

	printf(“Successfully allocated and wrote to memory\n”);
	return 0;
}
 
