How to Run?:
python Run.py

CommandParser.py:
	* What does it do?
	- Read one line (or command)
	* Assumption:

Execute.py:
	* What does it do?
	- Parse raw string command
	- Issue execute operation/Command
	* Assumption:
	- Assuming commands are case sensitive; hence discarding what not 
	  I don't recognize (KNOWN_COMMANDS) - error - "Invalid Command"
	- If there are more arguments than expected; ignore
	- If the command isn't complete - or in other words less arguments 
	  then don't do anything Error out - "Invalid Command"

Database.py
	* What does it do?
	- This class takes care of in-memory database operation
	- It stores two things:
	  1) Stack of pending transactions - top being newest transaction
	     I keep Transaction Block as dictionary to achieve O(1)
		 for GET, SET, UNSET
		 Key=Variable name,  Value=Variable Value
	  2) Stack of value counter - top being newest counter of value
		 Same as (1). Its a stack of dictionary, key=value, Value=
		 # of times value occurred till current transaction block
	  Both of them are stack so that when Rollback occurs I can just
	  throw away TOP (the newest transaction)
	* Assumption
	- Set:
		If no open transaction then assume we've opened one


Algorithm:
-----------------
|   Current     |          {Var: val1, Var: val2 ...} -> Transaction Info
|	Transaction |--------> {Val1: count1, val2: count2 ...} -> Value counter 
|	- say ith   |
-----------------
|   Previous    |
|	Transaction |
|	(i - 1)     |
|---------------| 				
| Transaction   |
|   (i-2)		|
|---------------|				
|  	And         |
|    so         |
|    on         |
|    .          |
|   ..			|
| 				|
|				|
|				|

* Each time Begin gets called two things happen:
1) Push new transaction(empty dict) info into transaction list
2) Push new value counter(empty dict) info into value counter list
* When GET gets called ..
- It looks for variable from TOP to bottom on stack of transactions
  As I have dictionary for any given transaction block it takes O(1)
  It will return current value of that variable
* NUMEQUALTO ..
- This is similar to GET, I look for value in current transaction (top
  of the stack) if not found go till I find in older transaction or
  till run out of list
* When SET gets called :
1) I call GET to get value of variable= old_value
2) In CURRENT transaction that old_value is getting replaced, hence
   I'll create/modify value_counter dict for old_value to be 
   num_ - 1. 
3) For CURRENT transaction a variable is getting new_value hence modify
   counter for new_value for CURRENT transaction to be new_value + 1
4) Add new variable into current transaction dict

e.g.
If I had earlier this stack,  :
transactio stack having 4 trans: [{}, {'a':10}, {'b':10}, {'c':10}, {'d': 40}]
value counter: [{}, {10: 3}, {10: 2}, {10: 1}, {40: 1}]

After SET a 40

It looks like this:
Transaction: [ {'a':40}, {'a':10}, {'b':10}, {'c':10}, {'d': 40} ]
Value Counter: [{40: 2, 10: 2}, {10: 3}, {10: 2}, {10: 1}, {40: 1}] 

* UNSET:
This simply calls SET var NONE.
* COMMIT:
Flatten both the stack (transaction and value counter)
- Create single transaction ..
Call all the open transation from older to newer so that we get NEWEST
- Create single value counter ..
Go through the just created one single transaction and create value
counter
Clear both the stack and push those new dict into their stack
* ROLLBACK:
Throw top from stack

