/*
Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

Hint:

How many variables do you need to keep track?
Two variables is all you need. Try with x and y.
Beware of empty rows. It could be the first few rows.
To write correct code, think about the invariant to maintain. What is it?
The invariant is x and y must always point to a valid point in the 2d vector. Should you maintain your invariant ahead of time or right when you need it?
Not sure? Think about how you would implement hasNext(). Which is more complex?
Common logic in two different places should be refactored into a common method.
*/

/**
class Vector2D {
public:
	int row, col;
	vector<vector<int>> data;
    Vector2D(vector<vector<int>>& vec2d) {
		data = vec2d;
        row = 0;
		col = 0;
    }

    int next() {
        return data[row][col++];
    }

    bool hasNext() {
       //Move to next row if a) no more data i.e. col = row.size b) no data anyway 
		while(row < data.size() && data[row].size() == col)
			row++; col = 0;
		return row < data.size();
    }
};

 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i(vec2d);
 * while (i.hasNext()) cout << i.next();
 */

////////////////////////////////
///////// WAY 2 //////////////
/////////////////////////////
class Vector2D {
public:
	vector<int> data;
	vector< vector<int> >::iterator row;
	vector<int>::iterator col;
	int i = 0;
    Vector2D(vector<vector<int>>& vec2d) {
  		for(row = vec2d.begin(); row != vec2d.end(); row++) {
			for(col = row->begin(); col != row->end(); col++) {
				data.push_back(*col);
			}
		}
    }

    int next() {
    	return data[i++]; 
    }

    bool hasNext() {
    	return (i < data.size());    
    }
};

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i(vec2d);
 * while (i.hasNext()) cout << i.next();
 */
