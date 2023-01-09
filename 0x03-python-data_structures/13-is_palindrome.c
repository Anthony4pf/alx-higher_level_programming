#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
*is_palindrome - check if a list is palindrome
*@head: pointer to the head node of the list
*Return: 1 if palindrome, 0 if not
*/

int is_palindrome(listint_t **head)
{
	listint_t *ptr = NULL;
	int count = 0, i = 0, j = 0;
	int *array;

	ptr = *head;

	if (ptr == NULL)
		return (1);

	while (ptr != NULL)
	{
		ptr = ptr->next;
		count++;
	}
	array = malloc(sizeof(int) * count);
	if (array == NULL)
		return (-1);

	ptr = *head;
	while (ptr != NULL)
	{
		array[i] = ptr->n;
		i++;
		ptr = ptr->next;
	}

	free(ptr);

	for (j = 0; j < count / 2; j++)
	{
		if (array[j] != array[count - j - 1])
		{
			free(array);
			return (0);
		}
	}

	free(array);
	return (1);
}
