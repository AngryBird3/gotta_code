/*
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
*/
/**
 * Definition for singly-linked list.
 */
#include <stddef.h>
#include <stdlib.h>
#include <iostream>
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

static void insert(ListNode* h, int val) {
	ListNode *p = h;
	while(p->next) {
		p = p->next;
	}	
	ListNode *n = new ListNode(val);
	p->next = n;
}

static void print_list(ListNode *h) {
	ListNode *p = h;
	while(p) {
		std::cout << p->val << ' ';
	 	p = p->next;
	}
	std::cout << std::endl;
}
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
		if(head == NULL || head->next == NULL || m == n) {
			return head;
		}
	
		ListNode *ret = new ListNode(-1);
		ret->next = head;
		ListNode *prev = ret;
	
		int i;
		for(i = 0; i < m-1; i++) {
			prev = head;
			head = head->next;
		}

		ListNode *rev = NULL;
		ListNode *cur = NULL;
		ListNode *nxt = NULL;

		/* Will set up mth's next pointer at the end */
		cur = prev->next;
		printf("prev: %d\n", prev->val);

        for(;i < n; i++) {
			printf("i: %d\n", i);
			nxt = cur->next;
			cur->next = rev;
			rev = cur;
			cur = nxt;	
			if(cur)
				printf("cur: %d rev:%d \n ", cur->val, rev ? rev->val : 0);
		} 
		
		//This is gonna set up first(mth val - which is now last) to cur pointer
		if (prev) {
			printf("prev->val: %d\n", prev->val);
		}
		prev->next->next = cur; 

		// This is setting up (m-1)th val to be reversed one (nth val)
		prev->next = rev;
		return ret->next;
    }
};

int main() {
	ListNode *t = new ListNode(1);
	insert(t, 2);
	insert(t, 3);
	//insert(t, 4);
	//insert(t, 5);
	//insert(t, 6);
	//insert(t, 7);
	//insert(t, 8);
	print_list(t);
	Solution sol = Solution();
	ListNode *res = sol.reverseBetween(t, 1, 3);
	print_list(res);
	return 0;
}
