#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * 
 * @list: Pointer to the head of  linked list.
 *
 * Return: If there is no cycle - 0.
 *	   Otherwise - 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
