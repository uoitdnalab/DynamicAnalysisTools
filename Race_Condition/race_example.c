//This file demonstrates a race condition from failure to synchronize threads

#include <stdio.h>
#include <pthread.h>

void *math_x(void *x_void_ptr)
{
	int *x_ptr = (int *)x_void_ptr;

	*x_ptr = *x_ptr * 2;

	printf(“DEBUG: math_x finished\n”);

	return NULL;
}

void *math_y(void *y_void_ptr)
{
	int *y_ptr = (int *)y_void_ptr;

	*y_ptr = *y_ptr * 10;

	printf(“DEBUG: math_y finished\n”);

	return NULL;
}

int main()
{
	int x = 10;
	int y = 50;

	pthread_t math_x_thread;
	pthread_t math_y_thread;

	pthread_create(&math_x_thread, NULL, math_x, &x); //math_x thread
	pthread_create(&math_y_thread, NULL, math_y, &y); //math_y thread


	int sum = x + y;

	printf(“The result of the calculation is %d\n”, sum);

	return 0;
}
 
