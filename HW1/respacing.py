# TODO: Your name, Cornell NetID
# TODO: Your Partner's name, Cornell NetID

# DO NOT CHANGE THIS CLASS
class RespaceTableCell:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.validate()

    # This function allows Python to print a representation of a RespaceTableCell
    def __repr__(self):
        return "(%s,%s)"%(str(self.value), str(self.index))

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.value) == bool), "Values in the respacing table should be booleans."
        assert(self.index == None or type(self.index) == int), "Indices in the respacing table should be None or int"

# Inputs: the dynamic programming table, indices i, j into the dynamic programming table, the string being respaced, and an "is_word" function.
# Returns a RespaceTableCell to put at position (i,j)
def fill_cell(T, i, j, string, is_word):
    #TODO: YOUR CODE HERE
    if (j == 0):
        return RespaceTableCell(False, 0)
    string = " " + string

    cellLeft = T.get(i,(j-1))
    if (i == j):
        # print("String value: " + string[i])
        if (cellLeft.value == True and cellLeft.index<0):
            if (is_word(string[i])):
                return RespaceTableCell(True, i)
            else:
                return RespaceTableCell(False, cellLeft.index)
        elif (cellLeft.value == True ):
            return RespaceTableCell(False, (j-1)*-1)
        elif (cellLeft.index<0):
            return RespaceTableCell(False, cellLeft.index)
        elif(is_word(string[i])):
            # print("Seen: "+ string[i])
            # v = RespaceTableCell(True, i)
            # print(v)
            return RespaceTableCell(True, i)
        else:
            return RespaceTableCell(False, i)

    tempString = string[j:i+1]
    # print(tempString)

    cellAbove = T.get((i-1), (j))

    #cellLeft = T.get(i,(j-1))
    if (is_word(tempString)):
        # if(cellLeft.value == True and cellLeft.index==-1):
        #     return RespaceTableCell(False, cellAbove.index)
        if(cellLeft.value == True ):
            # return RespaceTableCell(False, -1)
            return RespaceTableCell(True, j*-1)
        elif(cellLeft.index <0):
            return RespaceTableCell(False, cellLeft.index)
        else:
            if (T.get(j, j).index < 0):
                return RespaceTableCell(True, j*-1)
            else:
                return RespaceTableCell(True, cellAbove.index)
    else:
        if (cellAbove.value == False or cellLeft.index<0 or cellLeft.value == True):
            if (cellLeft.index <0 and cellLeft.value ==True):
                # return RespaceTableCell(False, j)
                if (cellAbove.index < 0):
                    return RespaceTableCell(False, i-1)
                else:
                    return RespaceTableCell(False, i - 1)
            elif(cellLeft.index <0 ):
                return RespaceTableCell(False, cellLeft.index)
            elif(cellLeft.value == True):
                return RespaceTableCell(False, (j-1)*-1)
            else:
                if( cellAbove.index < 0):
                    return RespaceTableCell(False, i-1)
                else:
                    return RespaceTableCell(False, cellAbove.index)
        else:
            if(cellAbove.index <0):
                return RespaceTableCell(False, i-1)
            else:
                return RespaceTableCell(False, i - 1)

# Inputs: N, the size of the list being respaced
# Outputs: a list of (i,j) tuples indicating the order in which the table should be filled.
def cell_ordering(N):
    #TODO: YOUR CODE HERE
    lst = []
    for col in range(N + 1):
        for row in range(col, N + 1):
            lst.append((row, col))

    #print(lst)
    return lst

# Input: a filled dynamic programming table.
# (See instructions.pdf for more on the dynamic programming skeleton)
# Return the respaced string, or None if there is no respacing.
def respace_from_table(s, table):
    i = len(s)
    j = i
    print(s)
    returnValue = ""
    checkValue = ""

    count = 0
    while(j!=0):
        # print(i)
        # print(j)
        startCell = table.get(i, j)
        # print j
        if(count==1):
            # print(startCell.index)
            returnValue = " " + s[j-1:row-1] + returnValue
            checkValue = s[j-1:row-1] + checkValue
            # print(startCell.index)
            count = 0
            row = len(s)
            j=j-1

        else:
            if (startCell.value == False):

                if(startCell.index<0):
                    j=j-1

                elif ( table.get(startCell.index,j).value==False ):
                    j= j-1

                else:
                    if (table.get(startCell.index,j).index>0):
                        returnValue = " " + s[j - 1:startCell.index] + returnValue
                        checkValue =  s[j - 1:startCell.index] + checkValue
                        # print(returnValue)
                        # print("Got Here")
                        # print(table.get(startCell.index, j))
                        j = j - 1


                    if (table.get(startCell.index,j).index<0):
                        # print(table.get(startCell.index,j))
                        column = (table.get((startCell.index), j)).index*-1


                        # column  = (table.get((table.get((startCell.index)*-1, j).index*-1, j).index))*-1
                        # row = table.get(table.get((startCell.index)*-1, j),column)
                        row = (startCell.index)
                        # print("Got Here")
                        if (table.get(row-1,column).value ==True and table.get(row,column).value ==True):

                            returnValue = " " + s[j - 1:(startCell.index)*-1] + returnValue
                            checkValue = s[j - 1:(startCell.index)*-1] + checkValue
                            j = column
                            i = row-1
                            count = count + 1
                        else:
                            j = j - 1

            else:
                if(startCell.index<0):

                    # column = (table.get((table.get((startCell.index)*-1, j).index*-1, j).index))*-1
                    column = (table.get((startCell.index) * -1, j)).index * -1
                    row = (startCell.index)*-1
                    # print("Got Here")
                    # if(column == j):
                    #     j=j-1

                    if(table.get(row-1,column).value == True):
                        returnValue = " " + s[j - 1:] + returnValue
                        checkValue = " " + s[j - 1:] + checkValue
                        # print("Reached Value!")
                        j = column
                        # print (j)
                        i = row - 1
                        count = count + 1
                    else:
                        j =j-1



                else:
                    returnValue = " " + s[j-1:i] + returnValue
                    checkValue =s[j - 1:i] + checkValue
                    j = j - 1

    returnValue = returnValue.lstrip()
    if (len(checkValue)<len(s)):
        return None
    else:
        return returnValue.lstrip()

if __name__ == "__main__":
    # Example usage.
    from dynamic_programming import DynamicProgramTable
    #s = "itwasthebestoftimes"
    #s = "catdog"
    # s = "ebonystoreblowvotestore"
    # s = "derekderekkdemedmed"
    # s = "wallsdoselatedoselate"
    # s = "bikeswhoooofeofgonna"
    # s = "crownwinewinewinsand"
    # s = "livehangtonydonalive"
    s = "mallsitllkleiknleinnis"

    # wordlist = ["ebony", "aruba", "vote", "store", "patio", "blow", "heads", "low", "birds", "note"]
    #wordlist = ["of", "it", "the", "best", "times", "was"]
    #wordlist = ["cat", "dog"]


    # wordlist = ["derek","med","kde"]
    # wordlist = ["ted","way","write","dose","kinds","late","walls","spot","irish","marsh"]
    # wordlist = ["labor","feof","ada","keno","sim","bikes","eur","who","ooo","gonna"]
    # wordlist = [ "crown","sand", "univ", "amino", "wins", "light", "usa", "wine", "keys", "win"]
    # wordlist = ["vast", "bands", "liked", "fully", "tent", "matt", "i", "store", "time", "joe"]
    # wordlist = ["alive","banks","live","spray","cafe","tony","maria","don","hang","hills"]
    wordlist = ["fair","klein","still","endif","const","dear","aruba","mall","ins","solar"]


    D = DynamicProgramTable(len(s) + 1, len(s) + 1, cell_ordering(len(s)), fill_cell)
    D.fill(string=s, is_word=lambda w:w in wordlist)
    for row in D._table:
        print (row)
    # print(D._table)
    print respace_from_table(s, D)
