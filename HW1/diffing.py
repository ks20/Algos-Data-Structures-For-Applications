# TODO: Your name, Cornell NetID
# TODO: Your Partner's name, Cornell NetID

import dynamic_programming

# DO NOT CHANGE THIS CLASS
class DiffingCell:
    def __init__(self, s_char, t_char, cost):
        self.cost = cost
        self.s_char = s_char
        self.t_char = t_char
        self.validate()

    # Helper function so Python can print out objects of this type.
    def __repr__(self):
        return "(%d,%s,%s)"%(self.cost, self.s_char, self.t_char)

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.cost) == int), "cost should be an integer"
        assert(type(self.s_char) == str), "s_char should be a string"
        assert(type(self.t_char) == str), "t_char should be a string"
        assert(len(self.s_char) == 1), "s_char should be length 1"
        assert(len(self.t_char) == 1), "t_char should be length 1"

# Input: a dynamic programming table,  cell index i and j, the input strings s and t, and a cost function cost.
# Should return a DiffingCell which we will place at (i,j) for you.
# def fill_cell(table, i, j, s, t, cost):


def fill_cell(table, i, j, s, t, cost):
    # TODO: YOUR CODE HERE

    s = '-'+s
    t = '-'+t

    if (i == 0 and j ==0):
        return None
    if (i == 0):
        if(j>1):
            addValue = table.get(i, (j-1))
            cost = cost('-',t[j])
            cost = addValue.cost + cost
            return DiffingCell('-',t[j], cost)

        else:
            cost = cost('-', t[j]) #where i == 0, j == 1
            return DiffingCell('-', t[j],  cost)

    if (j == 0):
        if (i > 1):
            addValue = table.get((i - 1), j)
            cost = cost(s[i],'-')
            cost = addValue.cost + cost
            return DiffingCell(s[i],'-', cost)

        else:
            cost = cost(s[i],'-')
            return DiffingCell(s[i],'-', cost)


    if (i==1 and j==1):
        costOne = cost(s[i], t[j])
        costTwo = (cost('-', t[j])) + table.get(i,j-1).cost
        costThree = (cost(s[i], '-')) + table.get(i-1,j).cost
        value_tuples = [
            (s[i], t[j], costOne),
            (s[i], '-', costThree),
            ('-', t[j], costTwo)
        ]

    else:
        costOne = (cost(s[i], t[j])) + table.get((i-1), (j-1)).cost
        costTwo = (cost('-', t[j])) + table.get(i, j-1).cost
        costThree = (cost(s[i], '-')) + table.get(i-1, j ).cost
        value_tuples = [
            (s[i], t[j], costOne),
            (s[i], '-', costThree),
            ('-', t[j], costTwo),
        ]

    value_tuples = sorted(value_tuples, key=lambda value: value[2])

    min = value_tuples[0]

    # print(value_tuples)
    # addValue = table.get((i-1), (j))

    # addValue = addValue.cost + min[2]

    return DiffingCell(min[0], min[1], min[2])

# Input: n and m, represents the sizes of s and t respectively.
# Should return a list of (i,j) tuples, in the order you would like fill_cell to be called
def cell_ordering(n,m):
    # TODO: YOUR CODE HERE
    lst = []
    for x in range(n+1):
        for y in range(m+1):
            lst.append((x, y))
    return lst

# Returns a size-3 tuple (cost, align_s, align_t).
# cost is an integer cost.
# align_s and align_t are strings of the same length demonstrating the alignment.
# See instructions.pdf for more information on align_s and align_t.
# def diff_from_table(s, t, table):
#     # TODO: YOUR CODE HERE
#
#     print(table._table)
#
#     j = len(s)
#     i = len(t)
#
#     align_s = ''
#     align_t = ''
#     returnValue = table.get(i, j)
#     while(i>=0 and j>=0):
#         if(i!=0 or j!= 0):
#             values = table.get(i, j)
#
#             if(values.s_char!='-' and values.t_char!='-'):
#                 align_s = values.s_char + align_s
#                 align_t = values.t_char + align_t
#                 i = i-1
#                 j = j-1
#             elif(values.s_char!='-' and values.t_char=='-'):
#                 j = j-1
#                 align_s = values.s_char + align_s
#                 align_t = values.t_char + align_t
#             elif (values.s_char == '-' and values.t_char != '-'):
#                 i = i - 1
#                 align_s = values.s_char + align_s
#                 align_t = values.t_char + align_t
#         else:
#             break
#     return (returnValue.cost, align_s, align_t)

def diff_from_table(s, t, table):
    # TODO: YOUR CODE HERE

    print(table._table)

    i = len(s)
    j = len(t)


    align_s = ''
    align_t = ''
    returnValue = table.get(i, j)
    while(i>=0 and j>=0):
        if(i!=0 or j!= 0):
            values = table.get(i, j)

            if(values.s_char!='-' and values.t_char!='-'):
                align_s = values.s_char + align_s
                align_t = values.t_char + align_t
                i = i-1
                j = j-1
            elif(values.s_char!='-' and values.t_char=='-'):
                i = i-1
                align_s = values.s_char + align_s
                align_t = values.t_char + align_t
            elif (values.s_char == '-' and values.t_char != '-'):
                j = j - 1
                align_s = values.s_char + align_s
                align_t = values.t_char + align_t
        else:
            break
    return (returnValue.cost, align_s, align_t)
# Example usage
if __name__ == "__main__":
    # Example cost function from instructions.pdf
    def costfunc(s_char, t_char):
        if s_char == t_char: return 0
        if s_char == 'a':
            if t_char == 'b': return 5
            if t_char == 'c': return 3
            if t_char == '-': return 2
        if s_char == 'b':
            if t_char == 'a': return 1
            if t_char == 'c': return 4
            if t_char == '-': return 2
        if s_char == 'c':
            if t_char == 'a': return 5
            if t_char == 'b': return 5
            if t_char == '-': return 1
        if s_char == '-':
            if t_char == 'a': return 3
            if t_char == 'b': return 3
            if t_char == 'c': return 3

    import dynamic_programming
    s = "acb"
    t = "baa"
    D = dynamic_programming.DynamicProgramTable(len(s) + 1, len(t) + 1, cell_ordering(len(s), len(t)), fill_cell)
    D.fill(s = s, t = t, cost=costfunc)
    (cost, align_s, align_t) = diff_from_table(s,t, D)
    print align_s
    print align_t
    print "cost was %d"%cost
