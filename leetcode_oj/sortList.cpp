/*
Sort a linked list in O(n log n) time using constant space complexity.
*/

/**
 * Definition for singly-linked list.
 */
#include <stdio.h>
#include <iostream>
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
public:
    ListNode* sortList(ListNode* head) {
    	if (!head) return NULL;

		if (!head->next) {
			return head;
		}
		//ListNode *a;
		//ListNode *b;
	
		//divide_list(head, a, b);

		ListNode *slow, *fast;
		ListNode *a, *b;		
		slow = head; fast = head;

		while(fast && fast->next) {
			slow = slow->next;
			fast = fast->next->next;
		}

		b = slow->next;
		a = head;
		slow->next = NULL;
		print_list(a);
		print_list(b);
		ListNode *ha = sortList(a);
		ListNode *hb = sortList(b);

		ListNode* sorted_head = merge_sorted(a, b);

		return sorted_head;
    }

	void print_list(ListNode* l) {
		while (l) {
			printf("%d ", l->val);
			l = l->next;
		}
		printf("\n");
	}
	/*
	 * Split into half, a= head, b=middle
     */
	void divide_list(ListNode* head, ListNode *a, ListNode *b) {
		if (!head or !head->next) {
			a = head;
			b = NULL;
		} 
		ListNode *slow, *fast;
		
		slow = head; fast = head;

		while(fast && fast->next) {
			slow = slow->next;
			fast = fast->next->next;
		}

		b = slow;
		a = head;
		slow->next = NULL;
	}

	/*
	 * Merge two sorted lists
	 * into one
	 */
	ListNode* merge_sorted(ListNode *a, ListNode *b) {
		ListNode* new_head = NULL;
		ListNode* prev = NULL;
		ListNode* head = NULL;
		while(a || b) {
			if (b->val < a->val) {
				head = b;
			} else {
				head = a;
			} 
			if (prev) {
				prev->next = head;
			} else {
				//This is going to be our new_head
				new_head = head;
			}
			prev = head;
			a = a->next;
			b = b->next;
		}
		return new_head;
	}
};

int main() {
	ListNode l5(5); ListNode l1(1); ListNode l4(4); ListNode l10(10);
	ListNode l2(2);
	l5.next = &l1;
	l1.next = &l4;
	l4.next = &l10;
	l10.next = &l2;
	
	Solution sol;
	ListNode* res = sol.sortList(&l4);
	
	while (res) {
		printf("%d ", res->val);
		res = res->next;
	}
	printf("\n");
}
