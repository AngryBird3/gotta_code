#include <stdio.h>
#include <iostream>
#include <set>
#include <stack>

struct node {
	int val;
	node *next;

	node(int v) { val = v; next = NULL;}
};

class LinkList {
	node *head;
	node *tail;
	public:
	LinkList() {head = NULL; tail = NULL;}
	void push_back(int v) {
		node *new_node = new node(v);
		if (!head) {
			head = new_node;
			tail = new_node;
		} else {
			tail->next = new_node;
			tail = new_node;
		}
	} 	

	void push_front(int v) {
		node *new_node = new node(v);
		if (!head) {
			head = new_node;
			tail = new_node;
		} else {
			new_node->next = head;
			head = new_node;
		}
	}

	void print_list() {
		node *h = head;
		node *n = head->next;
		while(h) {
			printf("%d->", h->val);
			h = h->next;
		}
		printf("\n");
	}

	node* getHead() {
		return head;
	}

	void remove_dup() {
		std::set<int> num;
		node* cur = head;
		node* prev = head;
		cur = cur->next;
		while (cur) {
			if (num.insert(cur->val).second == true) {
				//Element doesn't exist in link list
				prev->next = cur;
				prev = cur;
			}
			cur = cur->next;
		}	
	}

	void remove_dup_no_space() {
		node* cur = head;
		node* prev = NULL;
		while(cur) {
			node* n = head;
			bool exists = false;
			while (n != cur) {
				if (n->val == cur->val) {
					exists = true;
					break;
				}
				n = n->next;
			}
			//Add to list if it didn't exist previously
			if (!exists) {
				if (prev) {
					prev->next = cur;
				} 
				prev = cur;
			} 
			cur = cur->next;
		}
	}

};

/*
add 2 huge numbers represented by linked list. Each linked list element represents a 4 digit number: 
linked list1 : 8798 -> 8765 -> 1243 -> 9856 -> 8888 -> 0914 
linked list 2: 8710 -> 5634 -> 1276 -> 8123 -> 1354 -> 9876 

output: ................-> ............. ..-> 7980->0243 -> 0790
*/
LinkList* add_two_list(LinkList* l1, LinkList *l2) {
	LinkList* l = new LinkList();
	// Reverse:
	std::stack<int> s1;
	std::stack<int> s2;
	node* p = l1->getHead();
	while(p) {
		s1.push(p->val);
		p = p->next;
	}	
	p = l2->getHead();
	while(p) {
		s2.push(p->val);
		p = p->next;
	}

	int c = 0;
	while(!s1.empty() || !s2.empty()) {
		//printf("Two num: %d & %d\n", s1.top(), s2.top());
		int res = s1.top() + s2.top() + c;
		s1.pop(); s2.pop();
		l->push_front(res % 10000);
		//printf("Val: %d\n", res % 10000);
		c = res / 10000;
	}
	
	while(!s1.empty()) {
		int res = s1.top() + c;
		s1.pop();
		l->push_front(res % 10000);
		c = res / 10000;
	}

	while(!s2.empty()) {
		int res = s2.top() + c;
		s2.pop();
		l->push_front(res % 10000);
		c = res / 10000;
	}

	return l;
}

int main() {
	/*
	LinkList *my_list = new LinkList();
	my_list->push_back(1);
	my_list->push_back(2);
	my_list->push_back(2);
	my_list->push_back(3);
	my_list->push_back(1);
	my_list->push_back(3);
	my_list->push_back(2);
	my_list->push_back(5);
	my_list->push_back(1);

	printf("My list:\n");
	my_list->print_list();
	my_list->remove_dup_no_space();
	printf("After removing duplicates my list:\n");
	my_list->print_list();
	*/
	LinkList l1; 
	l1.push_back(8798);
	l1.push_back(8765);
	l1.push_back(1243);
	l1.push_back(9856);
	l1.push_back(8888);
	l1.push_back(914);

	LinkList l2;
	l2.push_back(8710);
	l2.push_back(5634);
	l2.push_back(1276);
	l2.push_back(8123);
	l2.push_back(1354);
	l2.push_back(9876);

	LinkList* l = add_two_list(&l1, &l2);
	l->print_list();
	return 0;
}
