#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	printf(“Hello, World\n”);
	printf(“Let’s try to allocate memory.\n”);

	char *buf = (char *)malloc(4);
	strcpy(buf,”He”); //No overflow

	free(buf); //Don’t leak memory

	strcpy(buf, “Hello, free pointer”); //Use-after-free

	printf(“Sucessfully allocated and wrote to memory\n”);
	return 0;
}
 
