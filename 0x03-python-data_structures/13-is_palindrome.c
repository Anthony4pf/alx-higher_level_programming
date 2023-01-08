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
	int count = 0, i = 0, j = 0, len = 0;
	int *l_array, *r_array;

	ptr = *head;	

	while (ptr != NULL)
	{
		ptr = ptr->next;
		count++;
	}

	l_array = malloc(sizeof(int) * count);
	r_array = malloc(sizeof(int) * count);

	temp = *head;
	len = count;

	while (temp != NULL)
	{
		l_array[i] = temp->n;
		r_array[count] = temp->n;
		i++;
		count--;
		temp = temp->next;
	}

	for (j = 0; i <= len; j++)
	{
		if (l_array[j] != r_array[j])
			return (1);
	}

	return (0);
}
