#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - function to check cycles
 * @list: list
 * Return: integer 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	a = list;
	b = list;
	while (a != NULL && b != NULL)
	{
		a = a->next;
		if (b->next)
			b = b->next->next;

		if (a == b)
			return (1);
	}
	return (0);
}
