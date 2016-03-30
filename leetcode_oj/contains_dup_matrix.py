# Enter your code here. Read input from STDIN. Print output to STDOUT
def containsDuplicate(n, mat, k):
    print "mat: ", mat, "k: ", k
    h = {}
    a = list()
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] in h:
                h[mat[i][j]].append((i,j))
                a.append(mat[i][j])
                #sorted(h[mat[i][j]], key=lambda x: x[0])
            else:
                h[mat[i][j]] = [(i, j)]
                
    for n in a:
        for i in range(len(h[n]) - 1):
            print "points: ",h[n][i], " and ", h[n][i+1]
            for j in range(i+1, len(h[n])):
                dist = manhattan_dist(h[n][i], h[n][i+1])
                print dist
                if dist <= k:
                    return "YES"
    return "NO"

def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
import sys
mat = []
#data = sys.stdin.readlines()
first = True
temp = 0
for line in sys.stdin:
	if temp:
		mat.append(map(int, line.split()))
		temp -= 1   
	else:
		k = int(line)
	if first:
		n = int(line)
		first = False
		temp = n
print containsDuplicate(n, mat, k)
