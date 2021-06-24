class Node:
    def __init__(self, table, parent):
        self.table = table
        self.parent = parent
        if parent == None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1

def goal_check(t, n, m, k):
    check = True
    for i in range(k):
        if len(t[i]) == n or len(t[i]) == 0:
            for j in range(len(t[i]) - 1):
                if t[i][j][1] == t[i][j+1][1] and int(t[i][j][0]) > int(t[i][j+1][0]):
                    continue
                else:
                    check = False
                    break
        else:
            check = False
            break
    return check

# making the new node by giving the parent and the movement
def make_node(node, k, l):
    new = []
    for i in range(len(node.table)):
        new.append([])
        for j in range(len(node.table[i])):
            new[i].append(node.table[i][j])
    new[l].append(new[k].pop())
    return Node(new, node)

def copy_node(node):
    new_node = Node(node.table, node.parent)
    return new_node

# getting inputs
n, m, k = input().split()
# number
n = int(n)
# colors
m = int(m)
# rows
k = int(k)
table = []
frontier = []
explored = []
answer = []
found = False
limit = 1
total = 0

# setting the table
for i in range(k):
    x = input()
    if x == '#':
        table.append([])
    else:
        table.append(x.split())

# checking if the table is our goal
if goal_check(table, n, m, k):
    print(table)
frontier.append(Node(table.copy(), None))

# increasing limit till the answer is found
while not found:
    explored = []
    frontier = []
    frontier.append(Node(table.copy(), None))
    total += 1
    # exploring new nodes while there are nodes in frontier and the answer is not found
    while len(frontier) > 0 and not found:

        # current exploring node index
        index = len(frontier) - 1
        # checking goal before exploring
        if goal_check(frontier[index].table, n, m, k):
            answer = copy_node(frontier[index])
            found = True
            break
        # checking if the frontier has touched the limit
        if frontier[index].depth < limit :
        # making new nodes
            for i in range(k):
                for j in range(k):

                    if i == j or len(frontier[index].table[i]) == 0:
                        continue
                    
                    # checking if the row is empty to move in
                    if len(frontier[index].table[j]) == 0:
                        temp_table = make_node(frontier[index], i ,j)
                        # checking if the node is in frontier or explored
                        if temp_table.table not in [n.table for n in explored] and temp_table.table not in [n.table for n in frontier]:
                            total += 1
                            frontier.append(copy_node(temp_table)) 
                        else:
                            continue
                    # checking if the rows last card is grater than the card to move in
                    elif int(frontier[index].table[i][-1][0]) < int(frontier[index].table[j][-1][0]):
                        temp_table = make_node(frontier[index], i ,j)
                        # checking if the node is in frontier or explored
                        if temp_table.table not in [n.table for n in explored] and temp_table.table not in [n.table for n in frontier]:
                            total += 1
                            frontier.append(copy_node(temp_table))
                        else:
                            continue
                    else:
                        continue
                if found:
                    break
        # adding node to explored list and removing from frontier
        explored.append(copy_node(frontier[index]))
        del frontier[index]
    limit += 1

#printing answer
if found :
    path = []
    depth= answer.depth
    for i in range(depth + 1):
        path.append(answer.table)
        answer = answer.parent

    for i in range(depth+1):
        print(path.pop())
        print('========>')

    print('depth = ', depth, ', explored : ', len(explored), ', total nodes created : ', total)
else :
    print('answer not found !!!')