//This file demonstrates a double-free memory vulnerability

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	printf(“Hello, World!\n”);
	printf(“Let’s try to allocate memory”);

	char *buf = (char *)malloc(4);
	strcpy(buf, “He”); //No overflow

	free(buf); //Don’t leak memory

	free(buf); //Double free

	printf(“Sucessfully allocated and wrote to memory\n”);
	return 0;
}
 
