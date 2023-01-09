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
	listint_t *ptr = NULL, *temp = NULL;
	int count = 0, i = 0, j = 0;
	int *l_array;
	
	ptr = *head;

	if (ptr == NULL)
		return (1);

	while (ptr != NULL)
	{
		ptr = ptr->next;
		count++;
	}
	l_array = malloc(sizeof(int) * count);
	if (l_array == NULL)
		return (-1);

	temp = *head;
	while (temp != NULL)
	{
		l_array[i] = temp->n;
		i++;
		temp = temp->next;
	}
	for (j = 0; j < count / 2; j++)
	{
		if (l_array[j] != l_array[count - j - 1])
		{
			free(l_array);
			return (0);
		}
	}
	free(l_array);
	return (1);
}
