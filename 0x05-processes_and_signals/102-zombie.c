#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - loops infinite
 * Return: 0 when ended
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates five zombies
 * Return: 0 exit
 */
int main(void)
{
	pid_t pid;
	int n = 0;

	while (n < 5)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		n++;
	}
	infinite_while();
	return (0);
}
