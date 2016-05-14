/*
Sort a linked list in O(n log n) time using constant space complexity.
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
            // If list size <= 1 - base case - terminate
            if (!head || !head->next) {
                return head;
            }
            ListNode* b = NULL;
            //Divide into two list only if there are more than two elements
            if (head->next->next) {
                ListNode* slow = head;
                ListNode* fast = head;

                while(fast && fast->next) {
                    slow = slow->next;
                    fast = fast->next->next;
                }
                b = slow->next;
                slow->next = NULL; //first list end
            } else {
                b = head->next;
                head->next = NULL;
            }

            return mergeLists(sortList(head), sortList(b));
    }
    
    ListNode* mergeLists(ListNode *a, ListNode *b) {
            ListNode *head = new ListNode(0); //Temp
            ListNode *ret = head;
        
            while(a && b) {
                if (a->val < b->val) {
                    head->next = a;
                    a = a->next;
                } else {
                    head->next = b;
                    b = b->next;
                }
                head = head->next;
            }

            while(a) {
                head->next = a;
                head = head->next;
                a = a->next;
            }

            while(b) {
                head->next = b;
                head = head->next;
                b = b->next;
            }
            //print_list(ret->next);
            return ret->next;
        }
};
